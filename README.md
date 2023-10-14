# News Fetcher Web App

News Fetcher is a web application that allows users to fetch and view news articles from various sources. It offers a user-friendly interface for searching news articles based on keywords, sources, categories, date range, and language.

## Features

- **User Authentication**: The application uses JWT (JSON Web Tokens) for user authentication. Users can sign up and log in to access personalized features.

- **Keyword-Based Search**: Users can search for news articles using keywords. The search parameters include keyword, sources, category, from date, to date, and language.

- **Caching for Improved Performance**: The application employs caching using Redis. It caches the API response for a specific set of search parameters, and if the same parameters are used within 15 minutes, the cached data is served, improving performance.

- **Refresh Button**: A "Refresh" button is provided, allowing users to fetch fresh news data, bypassing the cache.

- **Dashboard**: Users have access to a dashboard where they can view their user details and the keywords they have searched for.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Backend**: Django (Python)
- **Authentication**: JWT (JSON Web Tokens)
- **Caching**: Redis
- **News API**: [NewsAPI](https://newsapi.org/)

## Installation

1. Clone the repository: `git clone https://github.com/ajayendrak/newsweb.git`

2. Change directory to the project folder: `cd newsweb`

3. Create a virtual environment (optional but recommended): `python -m venv venv`

4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

5. Install project dependencies: `pip install -r requirements.txt`

6. Create a `.env` file in the project directory and add your environment variables, including your NewsAPI key.

   Example `.env` file:

   ```env
   DEBUG=True
   NEWS_API_KEY=your-newsapi-key


Apply database migrations: python manage.py migrate

Start the Django development server: python manage.py runserver

Access the application in your web browser at http://localhost:8000/

Usage
Sign up for a new account or log in if you already have one.

Enter search criteria on the home page, such as keywords, sources, category, date range, and language.

Click the "Search" button to fetch news articles matching the criteria.

To refresh and fetch fresh data, click the "Refresh" button.

Access your dashboard by clicking the "Dashboard" button to view your user details and search history.

Acknowledgments
This project uses the NewsAPI to fetch news data.

License
This project is open-source and available under the MIT License.
