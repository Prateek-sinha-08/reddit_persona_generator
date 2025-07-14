Follow these steps to run the Reddit Persona Generator for any Reddit user:


1. Clone the Repository
----------------------------------------------
git clone https://github.com/Prateek-sinha-08/reddit_persona_generator.git
cd reddit_persona_generator


2. Create a Virtual Environment (Recommended)
----------------------------------------------
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Dependencies
----------------------------------------------
pip install -r requirements.txt


4. Set Up Your .env File
----------------------------------------------
Create a file named .env in the project root with the following content:
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=reddit_persona_app
GROQ_API_KEY=your_groq_api_key

You can get Reddit API keys from https://www.reddit.com/prefs/apps
Get your Groq API key from https://console.groq.com

5. Run the Script for Any Reddit Profile
----------------------------------------------
Use the following command:
python run.py --username <reddit_username>
Example:
python run.py --username kojied


6. View the Output
----------------------------------------------
After successful execution, you will get the output file in the outputs folder.
