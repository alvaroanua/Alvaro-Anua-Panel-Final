#Función principal del Chatbot
function handle_user_query(query):
    # Procesar la consulta del usuario con NLP
    intent, parameters = NaturalLanguageProcessing.process(query)

    # Manejar diferentes intenciones del usuario
    if intent == "consult_calendar":
        return consult_calendar(parameters)
    elif intent == "send_message":
        return send_message(parameters)
    elif intent == "check_compatibility":
        return check_compatibility(parameters)
    elif intent == "calculate_estimated_time":
        return calculate_estimated_time(parameters)
    elif intent == "sort_tasks_by_urgency":
        return sort_tasks_by_urgency(parameters)
    else:
        return "Lo siento, no entiendo la solicitud. ¿Puedes reformularla?"

# Función para consultar el calendario del usuario
consult_calendar(parameters):
    # Obtener el usuario
    user_id = get_user_id(entities)
    # Eventos del calendario
    events = model.get("/users/" + user_id + "/calendar/events")
    # Devolver lista de fechas con eventos
    return format_events(events)

# Función para enviar un mensaje
function send_message(parameters):
    # Obtener el receptor del mensaje (email al que se envia)
    email = get_email(parameters)
    # Obtener el msg
    message = get_message(parameters)
    # Pedir al modelo el post
    model.post("/users/" + email + "/sendMail", message)

    return "Mensaje enviado exitosamente."

# Función para consultar la compatibilidad de horarios
function check_compatibility(parameters):
    # Obtener que personas van a asistir a la reunion
    users = get_users(parameters)
    # Recuperar los slots de tiempo del calendar a traves del modelo de los usuarios
    time_slots = model.get("/me/calendar/getSchedule", {"schedules": users})
    # Comparar huecos disponibles entre los usuarios
    free_slots = get_free_slots(time_slots)
    return free_slots

# Función para calcular el tiempo estimado de una tarea
function calculate_estimated_time(parameters):
    # Recuperar las tasks pendientes de realizar
    tasks_id = get_tasks_id(parameters)
    # Obtener datos de la task (entre otras tiempo estimado)
    task_details = model.get("/planner/tasks/" + tasks_id)
    # Recuperar el tiempo estimado de todas las tareas
    estimated_time = calculate_time(task_details)
    # Tiempo laboral disponible del usuario
    disponibility = model.get("/planner/free_slots/")
    # Metodo que devuelva que dia se espera que termines teniendo en cuenta disponibility y estimated_time
    finish_date = calculate_finish(disponibility. estimated_time)
    # Devolver la estimacion al modelo
    return finish_date
