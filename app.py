from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m * height_m)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obesity"
    else:
        return "Severe Obesity"


def get_guidance(category):
    guidance = {
        "Underweight": {
            "workout": "Light strength training, walking and gentle exercises.",
            "yoga": "Bhujangasana, Vajrasana, Trikonasana and gentle stretching.",
            "nutrition": "Focus on nutritious calorie-rich foods, protein, fruits, vegetables and whole grains."
        },

        "Normal": {
            "workout": "Regular walking, jogging, cycling and moderate strength training.",
            "yoga": "Surya Namaskar, Trikonasana, Setu Bandhasana and regular stretching.",
            "nutrition": "Maintain a balanced diet with vegetables, fruits, protein and whole grains."
        },

        "Overweight": {
            "workout": "Brisk walking, cycling, swimming and moderate strength training.",
            "yoga": "Surya Namaskar, Trikonasana, Setu Bandhasana and gentle stretching.",
            "nutrition": "Focus on vegetables, fruits, lean protein and whole grains while limiting excess sugar and highly processed foods."
        },

        "Obesity": {
            "workout": "Start with walking and low-impact exercises. Gradually increase activity.",
            "yoga": "Gentle yoga, breathing exercises and simple stretching.",
            "nutrition": "Focus on vegetables, fruits, lean protein and whole grains. Limit sugary and highly processed foods."
        },

        "Severe Obesity": {
            "workout": "Begin with gentle walking and low-impact exercises. Consider professional guidance before increasing intensity.",
            "yoga": "Gentle yoga, breathing exercises and comfortable stretching.",
            "nutrition": "Choose balanced meals with vegetables, fruits, protein and whole grains. Consider consulting a healthcare professional for personalized advice."
        }
    }

    return guidance[category]


@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None
    guidance = None
    error = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            if weight <= 0 or height <= 0:
                error = "Please enter valid positive values."

            else:
                bmi = round(calculate_bmi(weight, height), 1)
                category = get_bmi_category(bmi)
                guidance = get_guidance(category)

        except (ValueError, KeyError):
            error = "Please enter valid numbers for weight and height."

    return render_template(
        "index.html",
        bmi=bmi,
        category=category,
        guidance=guidance,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)