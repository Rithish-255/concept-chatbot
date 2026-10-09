import re

CONCEPTS = {
    "ai": {
        "title": "Artificial Intelligence (AI)",
        "answer": "Artificial Intelligence (AI) is the field of computer science focused on building systems that can perform tasks normally requiring human intelligence, such as reasoning, learning, problem-solving, and decision-making.",
        "points": [
            "AI includes machine learning, deep learning, and rule-based systems.",
            "It is used in virtual assistants, recommendation systems, robotics, and healthcare.",
            "AI aims to automate tasks that require human-like thinking."
        ]
    },
    "machine learning": {
        "title": "Machine Learning (ML)",
        "answer": "Machine Learning is a branch of AI that teaches computers to learn patterns from data instead of being explicitly programmed for each task.",
        "points": [
            "It uses training data to identify patterns and make predictions.",
            "Common techniques include supervised learning, unsupervised learning, and reinforcement learning.",
            "Examples include spam detection, recommendation engines, and image recognition."
        ]
    },
    "python": {
        "title": "Python",
        "answer": "Python is a simple, readable, and powerful programming language widely used in web development, data science, automation, AI, and scripting.",
        "points": [
            "It has a clean syntax that is easy to learn.",
            "It supports object-oriented, functional, and procedural programming.",
            "It has a large ecosystem of libraries such as NumPy, Pandas, and TensorFlow."
        ]
    },
    "oop": {
        "title": "Object-Oriented Programming (OOP)",
        "answer": "Object-Oriented Programming is a programming approach where software is organized around objects, each containing data and behavior.",
        "points": [
            "Core concepts include classes, objects, inheritance, encapsulation, and polymorphism.",
            "OOP helps manage code complexity and promotes reusability.",
            "It is commonly used in large-scale software systems."
        ]
    },
    "dbms": {
        "title": "DBMS",
        "answer": "DBMS stands for Database Management System. It is software used to create, manage, and retrieve data efficiently from databases.",
        "points": [
            "Examples include MySQL, PostgreSQL, Oracle, and MongoDB.",
            "It helps organize structured data and supports queries.",
            "DBMS ensures data integrity, security, and consistency."
        ]
    },
    "networking": {
        "title": "Networking",
        "answer": "Networking refers to the communication between connected devices so they can share information and resources.",
        "points": [
            "It includes concepts such as IP addresses, protocols, routers, and switches.",
            "Common protocols include HTTP, TCP/IP, and DNS.",
            "Networking enables internet communication and local area networks."
        ]
    },
    "algorithm": {
        "title": "Algorithm",
        "answer": "An algorithm is a step-by-step procedure or formula used to solve a problem or perform a computation.",
        "points": [
            "Algorithms are the foundation of computer science.",
            "They can be simple, like sorting numbers, or complex, like route optimization.",
            "Efficiency is often measured using time and space complexity."
        ]
    },
    "cybersecurity": {
        "title": "Cybersecurity",
        "answer": "Cybersecurity is the practice of protecting systems, networks, and data from cyberattacks, unauthorized access, and damage.",
        "points": [
            "It includes authentication, encryption, malware prevention, and firewalls.",
            "It is essential for protecting digital infrastructure.",
            "Examples include phishing protection and secure password management."
        ]
    }
}


def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def find_topic(user_input):
    normalized = normalize(user_input)
    for key in CONCEPTS:
        if key in normalized:
            return key
    return None


def display_concept(topic):
    info = CONCEPTS[topic]
    print(f"\n{info['title']}: {info['answer']}")
    print("Key points:")
    for point in info["points"]:
        print(f"- {point}")


def chatbot():
    print("Welcome to Concept Chatbot!")
    print("Ask a question about a topic such as AI, Machine Learning, Python, OOP, DBMS, Networking, Algorithm, or Cybersecurity.")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() in {"exit", "quit", "bye", "stop"}:
            print("Bot: Goodbye! Keep learning.")
            break

        if not user_input.strip():
            print("Bot: Please enter a valid question.")
            continue

        topic = find_topic(user_input)

        if topic:
            display_concept(topic)
        elif "hello" in normalize(user_input) or "hi" in normalize(user_input):
            print("Bot: Hello! I can explain technology concepts. Ask me about AI, Python, DBMS, OOP, or Networking.")
        else:
            print("Bot: I can help with common technology topics. Try asking about AI, Machine Learning, Python, OOP, DBMS, Networking, Algorithms, or Cybersecurity.")


if __name__ == "__main__":
    chatbot()

