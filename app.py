from flask import Flask, render_template, request
from calculator_exchangeFinal import calculate_final_score
import logging
import os

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        results = []
        for i in range(1, 5):  # Process inputs for up to 4 users
            # Get form data
            grade = request.form.get(f'grade{i}', '').strip()
            ibt = request.form.get(f'ibt{i}', '').strip()
            itp = request.form.get(f'itp{i}', '').strip()
            ielts = request.form.get(f'ielts{i}', '').strip()
            bonus = request.form.get(f'bonus{i}', '').strip()

            # Skip processing if all fields are empty for a user
            if not (grade or ibt or itp or ielts or bonus):
                continue

            # Handle empty values
            grade = float(grade) if grade else 0
            ibt = float(ibt) if ibt else None
            itp = int(itp) if itp else None
            ielts = float(ielts) if ielts else None
            bonus = float(bonus) if bonus else 0

            # Debug log input values
            logging.debug(f"Inputs for user {i}: grade={grade}, ibt={ibt}, itp={itp}, ielts={ielts}, bonus={bonus}")

            # Calculate final score
            try:
                final_score = calculate_final_score(grade=grade, ibt=ibt, itp=itp, ielts=ielts, bonus=bonus)
            except Exception as calc_error:
                logging.error(f"Error in calculate_final_score for user {i}: {calc_error}")
                final_score = "Calculation Error"

            # Append results
            results.append({
                'grade': grade,
                'ibt': ibt or "N/A",
                'itp': itp or "N/A",
                'ielts': ielts or "N/A",
                'bonus': bonus,
                'final_score': final_score
            })

        # If no users provided valid inputs, display an error
        if not results:
            return "No valid inputs provided. Please fill out at least one user's details.", 400

        # Debug log results
        logging.debug(f"Final results: {results}")

        return render_template('result.html', results=results)
    except Exception as e:
        logging.error(f"Error processing form data: {e}")
        return f"오류가 발생했습니다: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
