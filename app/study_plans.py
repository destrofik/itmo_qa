# Временное решение
study_plans = {
    "ai": {
        "description": "Магистерская программа 'Искусственный интеллект'. Включает курсы по машинному обучению, глубокому обучению, компьютерному зрению.",
        "courses": [
            "Машинное обучение",
            "Глубокое обучение",
            "Компьютерное зрение",
            "Обработка естественного языка"
        ]
    },
    "ai_product": {
        "description": "Магистерская программа 'AI Product'. Фокусируется на продуктовой разработке AI-систем, управлении проектами и интеграции AI в бизнес.",
        "courses": [
            "Управление продуктом",
            "Аналитика данных",
            "Разработка AI-продуктов",
            "Маркетинг AI-решений"
        ]
    }
}

def get_plan(program_key: str):
    return study_plans.get(program_key.lower())
