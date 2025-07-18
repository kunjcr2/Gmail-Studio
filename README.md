# 📧 Gmail Studio

A comprehensive Gmail analytics dashboard built with Python and Streamlit, similar to YouTube Studio but for Gmail accounts.

## 🚀 Features

- **User Authentication**: Secure login/register system with MongoDB
- **Gmail Integration**: Connect your Gmail account via Google API
- **Comprehensive Analytics**:
  - Email volume over time
  - Sender analysis and top domains
  - Time-based patterns (hourly, daily, weekly)
  - Email categories and labels
  - Thread/conversation analytics
  - Email size distribution
- **Beautiful Visualizations**: Interactive charts using Plotly
- **Real-time Data**: Refresh analytics on demand

## 📊 Analytics Dashboard

The dashboard provides insights into:

- **Key Metrics**: Total emails, unique senders, average daily volume, total storage
- **Time Analysis**: Daily email volume trends, hourly distribution, day-of-week patterns
- **Sender Analysis**: Top email senders and domains
- **Category Analysis**: Gmail label distribution
- **Thread Analytics**: Conversation patterns and engagement metrics
- **Raw Data**: Detailed email data table

## 🛠️ Setup Instructions

### 1. Prerequisites

- Python 3.7+
- MongoDB instance
- Google Cloud Project with Gmail API enabled

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the project root with the following variables:

```env
# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/
DB_NAME=gmail_studio
COLLECTION_USERS=users

# Gmail API Configuration
# Option 1: Service Account (recommended for production)
GOOGLE_SERVICE_ACCOUNT_PATH=path/to/your/service-account-key.json

# Option 2: OAuth2 Client (for development)
# You'll need to create credentials.json from Google Cloud Console
```

### 4. Gmail API Setup

#### Option A: Service Account (Recommended)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Gmail API
4. Create a Service Account
5. Download the JSON key file
6. Set the path in `GOOGLE_SERVICE_ACCOUNT_PATH` environment variable

#### Option B: OAuth2 Client

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create OAuth2 credentials
3. Download the credentials file as `credentials.json`
4. Place it in the project root

### 5. Run the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 🔐 Authentication Flow

1. **User Registration/Login**: Create an account or login using the sidebar
2. **Gmail Connection**: Click "Connect Gmail Account" to authenticate with Gmail
3. **Analytics**: Click "Refresh Analytics" to load your Gmail data
4. **Dashboard**: Explore your email analytics with interactive charts

## 📈 Analytics Features

### Email Volume Analysis

- Daily email trends
- Hourly distribution patterns
- Day-of-week analysis

### Sender Insights

- Top email senders
- Domain distribution
- Unique sender count

### Category Analysis

- Gmail label distribution
- Email categorization

### Thread Analytics

- Conversation patterns
- Thread duration analysis
- Message count per thread

### Storage Analysis

- Email size distribution
- Total storage usage
- Average email size

## 🎨 UI Features

- **Responsive Design**: Works on desktop and mobile
- **Interactive Charts**: Hover for details, zoom, pan
- **Real-time Updates**: Refresh data without page reload
- **Clean Interface**: Modern, professional design
- **Session Management**: Persistent login state

## 🔧 Customization

### Adding New Analytics

To add new analytics, modify the `GmailData.py` file:

1. Add new methods to the `GmailData` class
2. Update the `get_email_analytics()` method
3. Add corresponding visualizations in `app.py`

### Styling

Customize the appearance by modifying the CSS in the `app.py` file:

```python
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Add more custom styles */
</style>
""", unsafe_allow_html=True)
```

## 🚨 Security Notes

- Store sensitive credentials in environment variables
- Use service accounts for production deployments
- Implement proper access controls for MongoDB
- Regularly rotate API keys

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the console for error messages
2. Verify your environment variables are set correctly
3. Ensure Gmail API is properly configured
4. Check MongoDB connection

## 🔮 Future Enhancements

- Email sentiment analysis
- Response time tracking
- Advanced filtering options
- Export functionality
- Email templates analysis
- Integration with other Google services
