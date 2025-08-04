# 🚀 EDA-GenAI Dashboard - Quick Setup Guide

> **5-Minute Setup for Professional EDA Dashboard with AI Insights**

## ⚡ Quick Start (5 Minutes)

### 1. **Clone & Install** (2 minutes)
```bash
git clone https://github.com/mubasshirahmed-3712/eda-genai-dashboard.git
cd eda-genai-dashboard
pip install -r requirements.txt
```

### 2. **Run Dashboard** (1 minute)
```bash
streamlit run app/eda_dashboard.py
```

### 3. **Access Dashboard** (1 minute)
```
🌐 Open: http://localhost:8501
📱 Network: http://your-ip:8501
```

### 4. **Optional: AI Setup** (1 minute)
```bash
# Install Ollama (if not installed)
# Visit: https://ollama.ai

# Pull Mistral model
ollama pull mistral

# Start Ollama service
ollama serve
```

## 🎯 What You Get

### 📊 **Professional EDA Dashboard**
- **📁 CSV Upload**: Upload your datasets or use built-in Titanic dataset
- **🧹 Smart Data Cleaning**: Handle missing values with multiple strategies
- **📈 Beautiful Visualizations**: 5+ plot types with dark theme
- **🤖 AI-Powered Insights**: Dual-mode analysis (AI + Basic)
- **📄 PDF Reports**: Professional downloadable reports

### 🎨 **Enhanced Features**
- **🌙 Dark Theme**: Professional, modern interface
- **📱 Responsive Design**: Works on all devices
- **💫 Smooth Animations**: Modern UI interactions
- **🎯 Intuitive Navigation**: Tab-based interface
- **📥 Multiple Downloads**: PNG, SVG, CSV, PDF formats

### 🤖 **AI Integration**
- **🧠 Dual Insight Modes**:
  - **AI-Powered**: Full analysis with Ollama/Mistral
  - **Basic Analysis**: Statistical insights without AI
- **🔧 Real-time Status**: Live Ollama connection monitoring
- **📋 Smart Fallback**: Works perfectly without AI
- **⚡ Enhanced Error Handling**: Clear troubleshooting guides

## 📖 Usage Guide

### 1. **📁 Data Upload**
- Upload your CSV file in the sidebar
- Or use the default Titanic dataset
- Automatic file validation and error handling

### 2. **🧹 Data Cleaning**
- Choose strategies for missing values:
  - **Numeric**: Mean/Median/Zero
  - **Categorical**: Mode/'Unknown'
- One-click cleaning with download option

### 3. **📊 Data Overview**
- View dataset metrics (rows, columns, missing values)
- Interactive data preview
- Data types and missing value analysis

### 4. **📈 Visualizations**
- **Plot Types**: Distribution, Boxplot, Countplot, Barplot, Correlation Heatmap
- **Smart Selection**: Automatic column filtering
- **Download Options**: High-res PNG and vector SVG
- **Enhanced Styling**: Large, professional plots

### 5. **🤖 AI Insights**
- **Choose Mode**: AI-powered or Basic analysis
- **Real-time Status**: See Ollama connection status
- **Comprehensive Analysis**: Data quality, patterns, recommendations
- **Fallback System**: Works without AI

### 6. **📄 Reports**
- Generate comprehensive PDF reports
- Download cleaned data as CSV
- Professional business-ready format

## 🔧 Troubleshooting

### Common Issues

#### **AI Insights Not Working**
```bash
# Check Ollama status
ollama list

# Start Ollama service
ollama serve

# Verify model
ollama pull mistral
```

#### **Port Already in Use**
```bash
# Use different port
streamlit run app/eda_dashboard.py --server.port 8502
```

#### **Missing Dependencies**
```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

### **AI Setup Troubleshooting**

#### **Ollama Not Found**
```bash
# Install Ollama
# Visit: https://ollama.ai/download

# Or use package manager
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.ai/install.sh | sh
```

#### **Model Not Available**
```bash
# List available models
ollama list

# Pull Mistral model
ollama pull mistral

# Check model status
ollama show mistral
```

#### **Connection Issues**
```bash
# Check if Ollama is running
netstat -an | grep 11434

# Restart Ollama service
ollama serve

# Test connection
curl http://localhost:11434/api/tags
```

## 🎨 Customization

### **Theme Customization**
Edit `assets/css/custom_style.css`:
```css
/* Change primary color */
.stButton > button {
    background-color: #YOUR_COLOR;
}

/* Modify gradients */
.plot-container {
    background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
}
```

### **Adding New Plot Types**
Extend `generate_plot()` in `app/eda_dashboard.py`:
```python
elif plot_type == "Your New Plot":
    # Add your custom plot logic
    sns.your_plot(data=df, x=x_col, y=y_col, ax=ax)
```

### **Custom AI Prompts**
Modify the prompt in `get_llm_insights()`:
```python
prompt = f"""
Your custom prompt here...
Dataset: {summary}
"""
```

## 🚀 Deployment Options

### **Local Development**
```bash
streamlit run app/eda_dashboard.py --server.port 8501
```

### **Streamlit Cloud**
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Deploy automatically

### **Docker Deployment**
```dockerfile
FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app/eda_dashboard.py"]
```

### **Heroku Deployment**
```bash
# Add Procfile
echo "web: streamlit run app/eda_dashboard.py --server.port=\$PORT" > Procfile

# Deploy
git push heroku main
```

## 📊 Performance Tips

### **Large Datasets**
- Use data sampling for initial analysis
- Clean data before visualization
- Consider using data caching

### **AI Performance**
- Reduce prompt complexity for faster responses
- Use basic analysis for quick insights
- Monitor Ollama resource usage

### **Memory Optimization**
- Clean data before loading into memory
- Use appropriate data types
- Consider chunked processing for large files

## 🔗 Quick Commands

### **Start Dashboard**
```bash
streamlit run app/eda_dashboard.py
```

### **Start with Custom Port**
```bash
streamlit run app/eda_dashboard.py --server.port 8502
```

### **Start Ollama Service**
```bash
ollama serve
```

### **Check Ollama Status**
```bash
ollama list
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Update Dependencies**
```bash
pip install -r requirements.txt --upgrade
```

## 📞 Support

### **Getting Help**
- **GitHub Issues**: [Create an issue](https://github.com/mubasshirahmed-3712/eda-genai-dashboard/issues)
- **Documentation**: Check the main README.md
- **Code Comments**: Inline documentation in the code

### **Common Questions**

**Q: Can I use the dashboard without AI?**
A: Yes! The basic analysis mode works perfectly without Ollama.

**Q: What file formats are supported?**
A: Currently CSV files. More formats coming soon!

**Q: How do I customize the theme?**
A: Edit `assets/css/custom_style.css` for visual changes.

**Q: Can I deploy this to production?**
A: Yes! Ready for Streamlit Cloud, Heroku, AWS, etc.

**Q: What's the difference between AI and Basic analysis?**
A: AI provides contextual insights, Basic provides statistical analysis.

---

## 🎉 You're All Set!

Your professional EDA dashboard is ready with:
- ✅ **Beautiful dark theme**
- ✅ **Advanced visualizations**
- ✅ **AI-powered insights**
- ✅ **Professional reporting**
- ✅ **Multiple export options**

**🚀 Start exploring your data now!**

---

<div align="center">

**Made with ❤️ by Mubasshir Ahmed for Data Scientists**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-FF6C37?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai/)

---

### **Connect with the Developer**
[![GitHub](https://img.shields.io/badge/GitHub-@mubasshirahmed--3712-181717?style=for-the-badge&logo=github)](https://github.com/mubasshirahmed-3712)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-@mubasshir3712-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mubasshir3712/)
[![Instagram](https://img.shields.io/badge/Instagram-@badhshah._09-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/badhshah._09)
[![Portfolio](https://img.shields.io/badge/Portfolio-Mubasshir's%20Portfolio-FF6B6B?style=for-the-badge&logo=vercel)](https://mubasshirsportfolio.vercel.app)

</div> 