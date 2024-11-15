import pyaudio
import wave
import speech_recognition as sr
from pydub import AudioSegment
import numpy as np
import time

class GrabadoraDeVoz:
    def __init__(self, umbral_silencio=1000, duracion_silencio=5, archivo_wav="grabacion.wav"):
        self.formato = pyaudio.paInt16
        self.canales = 1
        self.tasa_muestreo = 16000
        self.tamaño_buffer = 1024
        self.umbral_silencio = umbral_silencio
        self.duracion_silencio = duracion_silencio
        self.archivo_wav = archivo_wav

    def grabar_audio(self):
        """Graba audio hasta que el usuario deje un silencio de 5 segundos"""
        # Crear objeto PyAudio
        p = pyaudio.PyAudio()
        
        # Abrir el flujo de audio
        flujo = p.open(format=self.formato, 
                      channels=self.canales, 
                      rate=self.tasa_muestreo, 
                      input=True, 
                      frames_per_buffer=self.tamaño_buffer)
        
        print("Grabando... (habla y deténte para finalizar)")
        
        # Variables para la grabación y la detección de silencio
        frames = []
        silencio_iniciado = False
        tiempo_silencio = 0
        
        while True:
            # Leer datos del flujo
            datos = flujo.read(self.tamaño_buffer)
            
            # Convertir los datos a un array numpy para análisis
            audio_data = np.frombuffer(datos, dtype=np.int16)
            
            # Calcular el volumen promedio
            volumen = np.abs(audio_data).mean()
            
            # Si el volumen es bajo (por debajo del umbral), contar como silencio
            if volumen < self.umbral_silencio:
                if not silencio_iniciado:
                    # Empezamos a contar el silencio
                    silencio_iniciado = True
                    tiempo_silencio = time.time()  # Iniciar temporizador del silencio
                elif time.time() - tiempo_silencio >= self.duracion_silencio:
                    # Si ya pasó 5 segundos de silencio, detener la grabación
                    print("Silencio detectado por 5 segundos, terminando grabación.")
                    break
            else:
                # Resetear el temporizador si se detecta sonido
                silencio_iniciado = False
            
            # Almacenar los frames grabados
            frames.append(datos)
        
        # Detener la grabación
        flujo.stop_stream()
        flujo.close()
        p.terminate()
        
        # Guardar el audio en un archivo WAV
        with wave.open(self.archivo_wav, 'wb') as archivo:
            archivo.setnchannels(self.canales)
            archivo.setsampwidth(p.get_sample_size(self.formato))
            archivo.setframerate(self.tasa_muestreo)
            archivo.writeframes(b''.join(frames))

        return self.archivo_wav

    def reconocer_voz(self):
        """Reconoce el texto del audio grabado"""
        r = sr.Recognizer()

        # Abrir el archivo de audio
        with sr.AudioFile(self.archivo_wav) as source:
            audio = r.record(source)

        # Reconocer el texto a partir del audio
        try:
            texto = r.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {texto}")
            return texto
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
            return None
        except sr.RequestError as e:
            print(f"Error de servicio; {e}")
            return None

    def convertir_a_mp3(self):
        """Convierte el archivo WAV a MP3"""
        audio = AudioSegment.from_wav(self.archivo_wav)

        # Guardar el archivo en formato MP3
        archivo_mp3 = self.archivo_wav.replace(".wav", ".mp3")
        audio.export(archivo_mp3, format="mp3")
        
        print(f"Archivo guardado como {archivo_mp3}")
        return archivo_mp3
