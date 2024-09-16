from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_message = ''
    if request.method == 'POST':
        midterm_grade = request.form.get('midterm_grade')
        prelim_grade = request.form.get('prelim_grade')

        try:
            prelim_grade = float(prelim_grade) if prelim_grade else None

            t_g = 75
            per_prelim = 0.20
            per_midterm = 0.30
            per_finals = 0.50

            if prelim_grade is not None and (prelim_grade < 0 or prelim_grade > 20):
                result_message = "The grade must be between 0 and 20."
            elif prelim_grade is not None:
                required_midterm_grade = (t_g - prelim_grade * per_prelim) * (per_midterm / (per_midterm + per_finals))
                required_final_grade = (t_g - prelim_grade) - required_midterm_grade
                result_message = (
                    f"- Congratulations, {midterm_grade}! Based on your current Prelim Grade of {prelim_grade:.2f}, you are required to achieve:<br><br>"
                    
                    f"- A minimum Midterm Grade of {required_midterm_grade:.2f} to remain on track for passing.<br><br>"
                                        
                    f"- A minimum Final Grade of {required_final_grade:.2f} to ensure successful completion of the course.<br><br>"
                                        
                    f"- Please note, {midterm_grade}, that with a Prelim Grade of {prelim_grade:.2f}, you are close to meeting the passing criteria. To ensure success, you must:<br><br>"
                                            
                    f"- Attain a minimum Midterm Grade of {required_midterm_grade:.2f}.<br><br>"
                                        
                    f"- Achieve a minimum Final Grade of {required_final_grade:.2f}."
                )
        except ValueError:
            result_message = "Invalid entry! Please enter a valid number or a appropriate character to proceed."

    return home_html(result_message)

def home_html(result_message):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Grading</title>
        <style>
        body {{ 
            margin: 0;
            padding: 0;
            font-family: Georgia; /* Changed to Georgia font */
            background: linear-gradient(to bottom, #008000, #000000);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #2F4F4F; /* Dark green text color */ 
         }}
    
        .container {{
            background: radial-gradient(#2F4F4F, #3E8E41);
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 30px;
            width: 400px;
            text-align: center;
            max-width: 90%;
            border: 2px solid #32CD32; /* Changed to thin light green border */
            border-style: solid; /* Add solid border lines */
         }}

        h1 {{
             color: #ffffff; /* Black text color */
             font-size: 28px;
             margin-bottom: 20px;
             text-shadow: 1px 1px 2px rgba(0,0,0,0.5); /* Added text shadow effect */
             font-family: "Times New Roman", cursive; /* Changed to Times New Roman font */
         }}

        input[type="text"],input[type="submit"]{{
            width: 100px;
            padding: 12px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #cccccc; /* Light gray border */
            font-size: 16px;
            box-sizing: border-box;
            outline: none;
            box-shadow: 0 0 0 2px #3498db inset; /* Change the inside color of the border to light blue */
            font-family: Monaco, monospace; /* Changed to Monaco font */
         }}

        input[type="text"]:focus{{
            border-color: #8e44ad; /* Purple border */
            background-color: #ffffff; /* White background */
            box-shadow: 0 0 10px rgba(0,0,0,0.5); /* Added box shadow effect */
            
         }} 

        input[type="submit"]{{
            background-color: #228B22; /* Dark green background */
            color: white;
            border-color: black; /* Black border */
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Added box shadow effect */
            font-family: Arial, sans-serif; /* Changed to Arial font */
         }} 

        input[type="submit"]:hover{{
            background-color: #c0392b; /* Darker red background */
            box-shadow: 0 0 10px rgba(0,0,0,0.5); /* Added box shadow effect */
        
         }}

        .result {{
            margin-top: 20px;
            font-size: 18px;
            color: #000000; /* Black text color */
            padding: 10px;
            border: 2px solid #32CD32; /* Green border */
            border-radius: 5px;
            background-color: #228B22; /* Dark green background */
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Added box shadow effect */
            font-family: Times New Roman, monospace; /* Changed to Times New Roman font */

        }}

        .header-box {{
           background-color: #228B22; /* Dark green background */
           border : 1px solid #000000; /* Black border */
           border-radius: 10px;
           padding: 10px;
           margin-bottom: 20px;
           box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Black box shadow effect */
           text-align: center; /* Center the header text */
           font-family: "Times New Roman", cursive; /* Changed to Times New Roman font */
           font-size: 36px; /* Increased font size */
           color: #000000; /* Black text color */
           text-shadow: 1px 1px 2px rgba(255, 255, 0, 0.5); /* Yellow text shadow effect */
         }}

        </style>
     </head>
    <body>    
        <div class="container">
            <div class="header-box">
                <h1>GRADE CALCULATOR</h1>
            </div>
            <form method="post">
                <div class="input-container">
                    <input type="text" name="midterm_grade" placeholder="Midterm">
                    <input type="text" name="prelim_grade" placeholder="Prelim">
                <input type="submit" value="Calculate">
            </form>
            <div class="result">{result_message}</div>
        </div>
    </body>   
    </html>
    """
    return html
if __name__ == '__main__':
    app.run(debug=True)