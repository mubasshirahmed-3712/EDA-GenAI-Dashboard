# 🔥 EDA-GenAI Dashboard

> **Professional, Real-World EDA Dashboard with AI-Powered Insights**.

A comprehensive, portfolio-grade Exploratory Data Analysis (EDA) dashboard built with Streamlit, featuring AI-powered insights using Ollama/Mistral, advanced visualizations, data cleaning capabilities, and professional PDF reporting.

![Dashboard Preview](assets/screenshots/dashboard-main.png)

## ✨ Features

### 🎯 **Core Functionality**
- **📁 CSV Upload & Default Dataset**: Upload your own CSV files or use the built-in Titanic dataset
- **🧹 Advanced Data Cleaning**: Handle missing values with multiple strategies (Mean/Median/Zero for numeric, Mode/'Unknown' for categorical)
- **📊 Professional Visualizations**: 5+ plot types with dark theme and enhanced styling
- **🤖 AI-Powered Insights**: Dual-mode insights (AI-powered with Ollama/Mistral + Basic statistical analysis)
- **📄 PDF Report Generation**: Comprehensive downloadable reports with dataset analysis

### 🎨 **Enhanced UI/UX**
- **🌙 Dark Theme**: Professional dark interface with custom CSS styling
- **📱 Responsive Design**: Optimized for all screen sizes
- **🎯 Intuitive Navigation**: Tab-based interface with clear sections
- **💫 Modern Animations**: Smooth transitions and hover effects
- **🎨 Beautiful Visualizations**: Large, high-quality plots with professional styling

### 🤖 **AI Integration**
- **🧠 Dual Insight Modes**:
  - **AI-Powered Analysis**: Full AI analysis using Ollama/Mistral
  - **Basic Statistical Analysis**: Comprehensive insights without AI dependency
- **🔧 Real-time Status**: Live Ollama connection status and troubleshooting
- **📋 Enhanced Error Handling**: Clear error messages and troubleshooting guides
- **⚡ Fallback System**: Works perfectly even when AI is unavailable

### 📈 **Advanced Visualizations**
- **📊 Distribution Plots**: Histograms with KDE for numeric data
- **📦 Boxplots**: Statistical distribution analysis
- **📊 Countplots**: Categorical data frequency analysis
- **📊 Barplots**: Relationship analysis between variables
- **🔥 Correlation Heatmaps**: Interactive correlation matrices
- **📥 Dual Download Options**: PNG (high-res) and SVG (vector) formats

### 📄 **Professional Reporting**
- **📋 Comprehensive PDF Reports**: Dataset summary, statistics, and analysis
- **📊 Data Overview**: Shape, memory usage, missing values analysis
- **📝 Data Types Analysis**: Column type distribution and insights
- **🔢 Statistical Summary**: Mean, median, std, min/max for numeric columns
- **📥 Download Options**: Cleaned data (CSV) and reports (PDF)

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Ollama (for AI-powered insights - optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mubasshirahmed-3712/eda-genai-dashboard.git
   cd eda-genai-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run app/eda_dashboard.py
   ```

4. **Access the dashboard**
   ```
   Local URL: http://localhost:8501
   Network URL: http://your-ip:8501
   ```

### Optional: AI Setup
For AI-powered insights, install and start Ollama:
```bash
# Install Ollama (if not already installed)
# Visit: https://ollama.ai

# Pull the Mistral model
ollama pull mistral

# Start Ollama service
ollama serve
```

## 📖 Usage Guide

### 1. 📁 Data Upload
![Data Upload](assets/screenshots/data-upload.png)
- **Upload CSV**: Use the sidebar file uploader to upload your dataset
- **Default Dataset**: Automatically loads Titanic dataset if no file is uploaded
- **File Validation**: Automatic error handling for invalid files

### 2. 🧹 Data Cleaning
![Data Cleaning](assets/screenshots/data-cleaning.png)
- **Numeric Strategy**: Choose Mean/Median/Zero for missing numeric values
- **Categorical Strategy**: Choose Mode/'Unknown' for missing categorical values
- **One-Click Cleaning**: Clean data with a single button click
- **Download Cleaned Data**: Export cleaned dataset as CSV

### 3. 📊 Data Overview
![Data Overview](assets/screenshots/data-overview.png)
- **Dataset Metrics**: Rows, columns, missing values, memory usage
- **Data Preview**: Interactive table with first 10 rows
- **Data Types**: Column type analysis and distribution
- **Missing Values**: Detailed missing value analysis with percentages

### 4. 📈 Visualizations
![Visualizations](assets/screenshots/visualizations.png)
- **Plot Types**: Distribution, Boxplot, Countplot, Barplot, Correlation Heatmap
- **Smart Column Selection**: Automatic column filtering based on plot type
- **Enhanced Styling**: Large, professional plots with dark theme
- **Download Options**: High-resolution PNG and vector SVG formats
- **Plot Information**: Detailed metadata about generated plots

### 5. 🤖 AI Insights
![AI Insights](assets/screenshots/ai-insights.png)
- **Dual Modes**: AI-powered (Ollama) or Basic statistical analysis
- **Real-time Status**: Live Ollama connection monitoring
- **Enhanced Prompts**: Professional, business-ready AI analysis
- **Comprehensive Coverage**: Data quality, patterns, opportunities, recommendations
- **Fallback System**: Works perfectly without AI

### 6. 📄 Reports
![Reports](assets/screenshots/reports.png)
- **PDF Generation**: Comprehensive downloadable reports
- **Dataset Summary**: Shape, cleaning results, missing values
- **Statistical Analysis**: Detailed numeric column statistics
- **Professional Format**: Business-ready report structure

## 🛠️ Technical Details

### Architecture
```
EDA-GenAI-Dashboard/
├── .streamlit/           # Streamlit configuration
├── app/                  # Main application
│   └── eda_dashboard.py  # Core dashboard application
├── assets/               # Static assets
│   ├── css/             # Custom styling
│   └── screenshots/     # Documentation images
├── data/                # Default datasets
├── reports/             # Generated reports storage
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

### Technologies Used
- **Frontend**: Streamlit, Custom CSS
- **Data Processing**: Pandas, NumPy
- **Visualization**: Seaborn, Matplotlib
- **AI Integration**: Ollama, Mistral Model
- **PDF Generation**: FPDF
- **Styling**: Custom CSS with dark theme

### Key Features Implementation
- **Session State Management**: Persistent data across interactions
- **Error Handling**: Comprehensive try-catch blocks with user-friendly messages
- **Responsive Design**: Mobile-friendly interface
- **Performance Optimization**: Efficient data processing and caching
- **Modular Architecture**: Clean, maintainable code structure

## 🎨 Customization

### Theme Customization
Edit `assets/css/custom_style.css` to customize:
- Color scheme and gradients
- Button styles and animations
- Layout spacing and typography
- Component-specific styling

### Adding New Plot Types
Extend the `generate_plot()` function in `app/eda_dashboard.py`:
```python
elif plot_type == "Your New Plot":
    # Add your custom plot logic here
    pass
```

### Custom AI Prompts
Modify the prompt in `get_llm_insights()` function for different analysis styles.

## 🚀 Deployment

### Local Development
```bash
streamlit run app/eda_dashboard.py --server.port 8501
```

### Cloud Deployment
The dashboard is ready for deployment on:
- **Streamlit Cloud**: Direct GitHub integration
- **Heroku**: Add `setup.sh` and `Procfile`
- **AWS/GCP**: Container-based deployment
- **Docker**: Use provided Dockerfile

### Environment Variables
```bash
# Optional: Custom Ollama endpoint
OLLAMA_ENDPOINT=http://localhost:11434

# Optional: Custom model name
OLLAMA_MODEL=mistral
```

## 🔧 Troubleshooting

### Common Issues

#### AI Insights Not Working
```bash
# Check if Ollama is running
ollama list

# Start Ollama service
ollama serve

# Verify model installation
ollama pull mistral
```

#### Port Already in Use
```bash
# Use different port
streamlit run app/eda_dashboard.py --server.port 8502
```

#### Missing Dependencies
```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

### Performance Tips
- **Large Datasets**: Use data sampling for initial analysis
- **Memory Issues**: Clean data before visualization
- **Slow AI Response**: Reduce prompt complexity or use basic analysis

## 📊 Screenshots

### Main Dashboard
![Main Dashboard](assets/screenshots/dashboard-main.png)
*Professional dark theme with intuitive navigation*

### Data Overview Tab
![Data Overview](assets/screenshots/data-overview-tab.png)
*Comprehensive dataset analysis with metrics and preview*

### Enhanced Visualizations
![Visualizations](assets/screenshots/visualizations-enhanced.png)
*Large, professional plots with download options*

### AI Insights with Status
![AI Insights](assets/screenshots/ai-insights-status.png)
*Dual-mode insights with real-time Ollama status*

### Reports Generation
![Reports](assets/screenshots/reports-generation.png)
*Professional PDF report generation*

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/mubasshirahmed-3712/eda-genai-dashboard.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt

# Run in development mode
streamlit run app/eda_dashboard.py --server.port 8501
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the amazing web framework
- **Ollama**: For local AI model hosting
- **Mistral AI**: For the powerful language model
- **Seaborn/Matplotlib**: For beautiful visualizations
- **Pandas**: For efficient data manipulation

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/mubasshirahmed-3712/eda-genai-dashboard/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mubasshirahmed-3712/eda-genai-dashboard/discussions)
- **Email**: mubasshir.ahmed3712@gmail.com

## 👨‍💻 About the Developer

<div align="center">

### **Mubasshir Ahmed**
*🧠 Data & AI Enthusiast | Python • SQL • ML • GenAI • BI Tools*

[![GitHub](https://img.shields.io/badge/GitHub-@mubasshirahmed--3712-181717?style=for-the-badge&logo=github)](https://github.com/mubasshirahmed-3712)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-@mubasshir3712-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mubasshir3712/)
[![Instagram](https://img.shields.io/badge/Instagram-@badhshah._09-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/badhshah._09)
[![Portfolio](https://img.shields.io/badge/Portfolio-Mubasshir's%20Portfolio-FF6B6B?style=for-the-badge&logo=vercel)](https://mubasshirsportfolio.vercel.app)

**🎓 BCA Graduate | Ex-Full Stack Dev | Est. 2004 | Proud Memon 🧬 | 📚 Lifelong Learner**

</div>

---

<div align="center">

**Made with ❤️ by Mubasshir Ahmed for the Data Science Community**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Ollama](https://img.shields.io/badge/Ollama-FF6C37?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai/)

---

### **Connect with Me**
[![GitHub](https://img.shields.io/badge/GitHub-@mubasshirahmed--3712-181717?style=for-the-badge&logo=github)](https://github.com/mubasshirahmed-3712)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-@mubasshir3712-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mubasshir3712/)
[![Instagram](https://img.shields.io/badge/Instagram-@badhshah._09-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/badhshah._09)
[![Portfolio](https://img.shields.io/badge/Portfolio-Mubasshir's%20Portfolio-FF6B6B?style=for-the-badge&logo=vercel)](https://mubasshirsportfolio.vercel.app)

</div> 