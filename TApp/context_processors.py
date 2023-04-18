from datetime import datetime

def fecha_actual(request):
    # Obtén la fecha actual
    fecha_actual = datetime.now().strftime('%d/%b/%Y')

    # Retorna un diccionario con la variable 'fecha' que estará disponible en el contexto de renderizado
    return {'fecha': fecha_actual}