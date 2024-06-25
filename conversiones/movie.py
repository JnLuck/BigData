from moviepy.editor import VideoFileClip

# Ruta del video original
video_path = "Download.mp4"

# Cargar el video original
video = VideoFileClip(video_path)

# Rotar el video verticalmente para que se vea horizontalmente
video = video.rotate(90)

# Definir el tiempo de inicio y fin del clip de 5 segundos
start_time = 0  # segundos
end_time = 5    # segundos

# Recortar el clip de 5 segundos
clip = video.subclip(start_time, end_time)

# Guardar el clip recortado
clip.write_videofile("Download2.mp4", codec="libx264")

# Liberar recursos
video.close()


