def classify_intent(text):
    text = text.lower()

    emergency_keywords = [
        "chest pain", "heart pain", "breathing difficulty", "shortness of breath", "can't breathe",
        "palpitations", "dizziness", "fainted", "fainting", "bleeding", "severe bleeding",
        "unconscious", "severe pain", "stroke", "attack", "tightness", "crushing pain",
        "accident", "burn", "cut", "wound", "trauma", "shock", "seizure", "convulsion",
        "electric shock", "snake bite", "choking", "loss of consciousness", "blue lips",
        "vomiting blood", "high fever", "severe headache", "confused", "not breathing", "emergency"
    ]

    medicine_keywords = [
        "medicine", "drug", "pill", "tablet", "capsule", "dose", "dosing", "dosage",
        "side effect", "paracetamol", "ibuprofen", "aspirin", "painkiller", "antibiotic",
        "antiviral", "antifungal", "med", "prescribed", "acetaminophen", "naproxen", 
        "safe to take", "contraindication", "interaction", "prescription", "fever reducer",
        "cold medicine", "headache medicine", "cough syrup", "allergy med", "injection", 
        "pregnancy safe medicine", "diabetes medicine", "blood pressure medicine", 
        "cholesterol medicine", "over the counter", "otc"
    ]

    nutrition_keywords = [
        "eat", "diet", "meal", "food", "nutrition", "nutrient", "nutritional", "balanced diet",
        "healthy food", "iron", "calcium", "vitamin", "zinc", "protein", "fiber",
        "what to eat", "low iron", "increase hemoglobin", "weight gain", "weight loss",
        "fruit", "vegetable", "hydration", "carbohydrate", "sugar", "low sugar",
        "blood sugar", "diabetic diet", "fat", "healthy fat", "cholesterol", "superfoods",
        "supplement", "multivitamin", "folic acid", "magnesium", "potassium", "omega 3",
        "home remedy", "food for fever", "immunity food", "eat on budget", "pregnancy diet"
    ]

    selfcare_keywords = [
        "self care", "selfcare", "stress", "mental health", "relax", "rest", "wellness",
        "healthy habits", "yoga", "meditate", "meditation", "mindfulness", "lifestyle",
        "routine", "burnout", "anxiety", "panic", "depression", "motivation", "tired", 
        "exhausted", "energy", "stay fit", "fitness", "workout", "exercise", "walk", 
        "hydration", "drink water", "sleep", "insomnia", "how to sleep", "calm", "focus",
        "mood", "tension", "peace", "emotional", "work-life balance", "stress relief"
    ]

    symptom_keywords = [
        "fever", "cough", "cold", "body ache", "pain", "headache", "sore throat", 
        "runny nose", "vomiting", "fatigue", "tired", "weakness", "chills", "dizzy", 
        "shortness of breath", "sweating", "rash", "itchy", "swelling", "infection",
        "high temperature", "mucus", "phlegm", "nausea", "symptoms", "signs of", 
        "sick", "not feeling well"
    ]

    
    for kw in emergency_keywords:
        if kw in text:
            return "Emergency"
    for kw in medicine_keywords:
        if kw in text:
            return "Medicine"
    for kw in nutrition_keywords:
        if kw in text:
            return "Nutrition"
    for kw in selfcare_keywords:
        if kw in text:
            return "SelfCare"
    for kw in symptom_keywords:
        if kw in text:
            return "Symptoms"

    return "General"
