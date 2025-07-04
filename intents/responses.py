def get_response(intent, question):
    question = question.lower()

    if intent == "Nutrition":
        if "hemoglobin" in question or "anemia" in question:
            return (
                "To naturally increase hemoglobin, focus on foods rich in iron, folate, and vitamin B12. "
                "Try spinach, pomegranates, dates, beetroot, lentils, and legumes. "
                "Eggs, red meat, and liver are excellent if you eat non-veg. Combine iron-rich foods with vitamin C (like citrus fruits) to boost absorption!"
            )
        elif "protein" in question:
            return (
                "Protein is key to muscle repair and overall health. Include sources like eggs, lentils, paneer, soy, dairy, chicken, and fish. "
                "You can also use protein-rich snacks like roasted chana or boiled eggs throughout the day."
            )
        elif "calcium" in question:
            return (
                "Dairy products like milk, cheese, and yogurt are top sources of calcium. "
                "Plant-based options include ragi, sesame seeds, tofu, almonds, and leafy greens like kale and spinach."
            )
        elif "weight gain" in question:
            return (
                "To gain weight healthily, eat calorie-dense but nutritious foods—peanut butter, bananas, whole milk, paneer, nuts, avocados, and eggs. "
                "Focus on strength training and eat more frequently throughout the day."
            )
        elif "weight loss" in question:
            return (
                "For weight loss, go for fiber-rich vegetables, lean proteins, and healthy fats. "
                "Cut down on refined carbs and sugary drinks. Stay active and eat mindfully—never skip meals!"
            )
        else:
            return (
                "Nutrition plays a big role in staying healthy! I can suggest diets for immunity, pregnancy, diabetes, or just overall well-being. "
                "Tell me what you're aiming for—weight gain, fatigue recovery, etc.—and I’ll guide you."
            )

    elif intent == "Medicine":
        if "paracetamol" in question or "acetaminophen" in question:
            return (
                "Paracetamol (acetaminophen) is generally safe when used as directed, even during pregnancy. "
                "However, avoid overdosing—stick to the recommended dosage and ask a doctor if unsure. Overuse may harm your liver."
            )
        elif "antibiotic" in question:
            return (
                "Antibiotics only work against bacterial infections. Taking them unnecessarily can lead to resistance. "
                "Always complete the prescribed course and don’t self-medicate without a doctor’s advice."
            )
        elif "ibuprofen" in question or "painkiller" in question:
            return (
                "Ibuprofen helps with pain and inflammation but may upset your stomach. Take it with food. "
                "Avoid if you have kidney issues, ulcers, or are in the third trimester of pregnancy."
            )
        elif "diabetes" in question:
            return (
                "There are several medicines for diabetes like metformin, glipizide, and insulin. "
                "Only a doctor can prescribe the right one based on your sugar levels and medical history."
            )
        elif "pregnancy" in question:
            return (
                "Some medicines are safe during pregnancy (like paracetamol), but others can be harmful. "
                "Always check with your gynecologist before taking anything new."
            )
        else:
            return (
                "Medication should always be taken with caution. Let me know the specific drug or symptom, and I can give general guidance!"
            )

    elif intent == "Emergency":
        if any(w in question for w in ["chest", "heart", "tightness", "pain"]):
            return (
                "Chest pain or tightness, especially with sweating or left-arm pain, could be a heart attack. "
                "Please call emergency services immediately. Do not delay—time matters in cardiac cases!"
            )
        elif any(w in question for w in ["breathing", "can't breathe", "shortness"]):
            return (
                "Breathing difficulties are serious and could be due to asthma, allergy, infection, or heart problems. "
                "If it's sudden or severe, seek medical help right away."
            )
        elif "fainted" in question or "unconscious" in question:
            return (
                "If someone fainted or is unconscious, lay them on their back, elevate their legs, and check for breathing. "
                "Call emergency services immediately and stay calm."
            )
        elif "bleeding" in question or "cut" in question:
            return (
                "Apply firm pressure on the wound with a clean cloth to stop bleeding. "
                "If it doesn’t stop or is deep, seek emergency care immediately."
            )
        elif "snake bite" in question:
            return (
                "In case of snake bite, keep the person still, avoid tying or cutting near the wound, and rush to a hospital immediately. "
                "Do not try to suck out the venom."
            )
        else:
            return (
                "This sounds serious. If someone is unconscious, bleeding heavily, or having breathing issues—please contact emergency services ASAP!"
            )

    elif intent == "SelfCare":
        if "sleep" in question or "insomnia" in question:
            return (
                "To improve sleep: set a consistent bedtime, avoid screens before bed, and try calming habits like reading, meditation, or warm tea. "
                "Make your sleeping space cool, dark, and quiet."
            )
        elif "stress" in question or "mental health" in question or "anxiety" in question:
            return (
                "Stress is common—try journaling, deep breathing, exercise, or talking to someone. "
                "Limit social media and include small joys like music, nature walks, or creative hobbies in your day."
            )
        elif "routine" in question or "habit" in question:
            return (
                "Building a healthy routine starts with consistency. Begin with small actions: wake up at the same time, drink water, stretch, and eat balanced meals. "
                "Routines give structure and peace to your day!"
            )
        elif "burnout" in question or "exhausted" in question:
            return (
                "You might be experiencing burnout—listen to your body. "
                "Take breaks, prioritize rest, talk to a friend, or delegate tasks. You don’t have to do everything alone."
            )
        else:
            return (
                "Self-care is about honoring your physical and emotional needs. "
                "Try simple steps—hydration, walking, quiet time, good sleep, saying 'no' when needed. Want a daily checklist?"
            )

    elif intent == "Symptoms":
        if "fever" in question:
            return (
                "Fever is usually a sign of infection. Rest, stay hydrated, and monitor your temperature. "
                "Paracetamol can reduce fever, but consult a doctor if it persists more than 3 days or is very high."
            )
        elif "cough" in question:
            return (
                "A cough can be dry or with mucus. Stay hydrated and try warm fluids. "
                "If it lasts over a week or comes with chest pain or high fever, see a doctor."
            )
        elif "fatigue" in question or "tired" in question:
            return (
                "Fatigue can be due to stress, poor diet, anemia, or even thyroid issues. "
                "Make sure you're eating well, sleeping enough, and staying active. If it persists, consult a doctor."
            )
        elif "rash" in question or "itchy" in question:
            return (
                "Skin rashes can be due to allergies, infections, or dryness. Try soothing creams and avoid triggers. "
                "If it spreads or becomes painful, seek medical attention."
            )
        else:
            return (
                "Symptoms like pain, fever, or tiredness can mean different things depending on the context. "
                "Please provide more details if you can, and I’ll help interpret it or suggest next steps."
            )

    else:
        return (
            "I'm here to support your health-related questions—whether it's about food, medicines, symptoms, or self-care. "
            "Try asking things like 'What to eat for low iron?' or 'How to sleep better?'"
        )
