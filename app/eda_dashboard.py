import streamlit as st
import pandas as pd
import numpy as np
try:
    import seaborn as sns
    print("✅ Seaborn is installed")
except ImportError as e:
    print(f"❌ Seaborn not found: {e}")

import matplotlib.pyplot as plt
from fpdf import FPDF
# import ollama  # For LLM Insights
import json
import io
import base64
from datetime import datetime
import os

# Set page config
st.set_page_config(
    page_title="EDA-GenAI Dashboard by Mubasshir Ahmed",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    try:
        with open('assets/css/custom_style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        # Fallback to inline CSS if file not found
        st.markdown("""
        <style>
        .main .block-container { padding-top: 2rem; padding-bottom: 2rem; }
        .stButton > button { background-color: #FF6B6B; color: white; border: none; border-radius: 8px; padding: 0.5rem 1rem; font-weight: 600; }
        .stButton > button:hover { background-color: #FF5252; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(255, 107, 107, 0.3); }
        .insight-card { background: linear-gradient(135deg, #2C3E50 0%, #34495E 100%); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border-left: 4px solid #FF6B6B; }
        </style>
        """, unsafe_allow_html=True)

load_css()

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'cleaned_data' not in st.session_state:
    st.session_state.cleaned_data = None

# Utility functions
def load_default_data():
    """Load default Titanic dataset"""
    try:
        return pd.read_csv('data/titanic_dataset.csv')
    except FileNotFoundError:
        # Fallback to seaborn's built-in titanic dataset
        import seaborn as sns
        return sns.load_dataset('titanic')
    except Exception as e:
        # Final fallback to seaborn's built-in titanic dataset
        import seaborn as sns
        return sns.load_dataset('titanic')

def clean_data(df, numeric_strategy='mean', categorical_strategy='mode'):
    """Clean the dataset based on user preferences"""
    df_cleaned = df.copy()
    
    # Handle numeric columns
    numeric_columns = df_cleaned.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        if df_cleaned[col].isnull().sum() > 0:
            if numeric_strategy == 'mean':
                df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mean())
            elif numeric_strategy == 'median':
                df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
            elif numeric_strategy == 'zero':
                df_cleaned[col] = df_cleaned[col].fillna(0)
    
    # Handle categorical columns
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        if df_cleaned[col].isnull().sum() > 0:
            if categorical_strategy == 'mode':
                mode_value = df_cleaned[col].mode()[0] if len(df_cleaned[col].mode()) > 0 else 'Unknown'
                df_cleaned[col] = df_cleaned[col].fillna(mode_value)
            elif categorical_strategy == 'unknown':
                df_cleaned[col] = df_cleaned[col].fillna('Unknown')
    
    return df_cleaned

def generate_plot(df, plot_type, x_col=None, y_col=None):
    """Generate different types of plots with enhanced styling"""
    # Set up the plotting style
    plt.style.use('dark_background')
    
    # Create a larger figure with better aspect ratio
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Set the background color
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#262730')
    
    # Color palette for better visual appeal
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']
    
    if plot_type == "Distribution Plot":
        if x_col and x_col in df.columns:
            if df[x_col].dtype in ['int64', 'float64']:
                # Enhanced histogram with KDE
                sns.histplot(data=df, x=x_col, kde=True, ax=ax, 
                           color=colors[0], alpha=0.7, edgecolor='white', linewidth=0.5)
                ax.set_title(f'Distribution of {x_col}', color='white', fontsize=18, fontweight='bold', pad=20)
                ax.set_xlabel(x_col, color='white', fontsize=14, fontweight='bold')
                ax.set_ylabel('Frequency', color='white', fontsize=14, fontweight='bold')
            else:
                # Enhanced countplot
                sns.countplot(data=df, x=x_col, ax=ax, color=colors[0], alpha=0.8)
                ax.set_title(f'Count of {x_col}', color='white', fontsize=18, fontweight='bold', pad=20)
                ax.set_xlabel(x_col, color='white', fontsize=14, fontweight='bold')
                ax.set_ylabel('Count', color='white', fontsize=14, fontweight='bold')
    
    elif plot_type == "Boxplot":
        if x_col and y_col and x_col in df.columns and y_col in df.columns:
            # Enhanced boxplot
            sns.boxplot(data=df, x=x_col, y=y_col, ax=ax, color=colors[1], width=0.7)
            ax.set_title(f'Boxplot: {y_col} by {x_col}', color='white', fontsize=18, fontweight='bold', pad=20)
            ax.set_xlabel(x_col, color='white', fontsize=14, fontweight='bold')
            ax.set_ylabel(y_col, color='white', fontsize=14, fontweight='bold')
    
    elif plot_type == "Countplot":
        if x_col and x_col in df.columns:
            # Enhanced countplot
            sns.countplot(data=df, x=x_col, ax=ax, color=colors[2], alpha=0.8)
            ax.set_title(f'Count of {x_col}', color='white', fontsize=18, fontweight='bold', pad=20)
            ax.set_xlabel(x_col, color='white', fontsize=14, fontweight='bold')
            ax.set_ylabel('Count', color='white', fontsize=14, fontweight='bold')
    
    elif plot_type == "Barplot":
        if x_col and y_col and x_col in df.columns and y_col in df.columns:
            # Enhanced barplot
            sns.barplot(data=df, x=x_col, y=y_col, ax=ax, color=colors[3], alpha=0.8)
            ax.set_title(f'Barplot: {y_col} by {x_col}', color='white', fontsize=18, fontweight='bold', pad=20)
            ax.set_xlabel(x_col, color='white', fontsize=14, fontweight='bold')
            ax.set_ylabel(y_col, color='white', fontsize=14, fontweight='bold')
    
    elif plot_type == "Correlation Heatmap":
        numeric_df = df.select_dtypes(include=[np.number])
        if len(numeric_df.columns) > 1:
            # Enhanced correlation heatmap
            correlation_matrix = numeric_df.corr()
            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
            sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='RdYlBu_r', 
                       center=0, ax=ax, square=True, linewidths=0.5, cbar_kws={"shrink": .8})
            ax.set_title('Correlation Heatmap', color='white', fontsize=18, fontweight='bold', pad=20)
    
    # Enhanced styling for all plots
    ax.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
    ax.tick_params(colors='white', labelsize=12)
    
    # Rotate x-axis labels if they're too long
    if plot_type in ["Countplot", "Barplot", "Boxplot"]:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    # Add some padding and tight layout
    plt.tight_layout(pad=2.0)
    
    return fig

def generate_pdf_report(df, cleaned_df):
    """Generate PDF report"""
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'EDA Dashboard Report', ln=True, align='C')
    pdf.ln(10)
    
    # Dataset Info
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Dataset Information:', ln=True)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 10, f'Original Shape: {df.shape}', ln=True)
    pdf.cell(0, 10, f'Cleaned Shape: {cleaned_df.shape}', ln=True)
    pdf.cell(0, 10, f'Missing Values: {df.isnull().sum().sum()}', ln=True)
    pdf.ln(5)
    
    # Summary Statistics
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Summary Statistics:', ln=True)
    pdf.set_font('Arial', '', 8)
    
    # Get numeric columns summary
    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        summary_stats = cleaned_df[numeric_cols].describe()
        for col in numeric_cols[:5]:  # Limit to first 5 columns
            pdf.cell(0, 8, f'{col}:', ln=True)
            pdf.cell(0, 6, f'  Mean: {summary_stats[col]["mean"]:.2f}', ln=True)
            pdf.cell(0, 6, f'  Std: {summary_stats[col]["std"]:.2f}', ln=True)
            pdf.cell(0, 6, f'  Min: {summary_stats[col]["min"]:.2f}', ln=True)
            pdf.cell(0, 6, f'  Max: {summary_stats[col]["max"]:.2f}', ln=True)
            pdf.ln(2)
    
    return pdf.output(dest='S').encode('latin-1')

def get_llm_insights(df):
    """Get insights from Ollama/Mistral using the ollama library"""
    try:
        import ollama  # Safely import Ollama inside function
        # Prepare dataset summary
        summary = {
            "shape": df.shape,
            "columns": list(df.columns),
            "dtypes": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "numeric_summary": df.describe().to_dict() if len(df.select_dtypes(include=[np.number]).columns) > 0 else {},
            "categorical_summary": {col: df[col].value_counts().head(5).to_dict() for col in df.select_dtypes(include=['object']).columns}
        }
        
        # Create a comprehensive prompt
        prompt = f"""
        You are a data scientist performing Exploratory Data Analysis (EDA). 
        Analyze this dataset and provide 3-5 key insights in a professional, business-ready format.
        
        Dataset Information:
        - Dataset Shape: {summary['shape']}
        - Columns: {summary['columns']}
        - Missing Values: {summary['missing_values']}
        
        Please provide insights covering:
        1. **Data Quality Assessment**: Comment on missing values, data types, and overall data quality
        2. **Key Patterns**: Identify any notable patterns or trends in the data
        3. **Analysis Opportunities**: Suggest potential areas for deeper analysis
        4. **Recommendations**: Provide actionable recommendations for data exploration
        
        Format your response in clear, professional language suitable for a business presentation.
        Use bullet points and clear sections for better readability.
        """
        
        # Use the ollama library for direct communication
        try:
            response = ollama.chat(
                model="mistral",
                messages=[{"role": "user", "content": prompt}],
                stream=False
            )
            
            insights = response.get('message', {}).get('content', '').strip()
            
            if insights:
                return insights
            else:
                return "🤖 AI generated an empty response. Please try again."
                
        except Exception as e:
            return f"""❌ **Ollama Connection Error**: {str(e)}
            
**Troubleshooting Steps:**
1. **Start Ollama**: Open a new terminal and run `ollama serve`
2. **Check Installation**: Run `ollama list` to see available models
3. **Verify Model**: Ensure Mistral model is pulled (`ollama pull mistral`)
4. **Restart Service**: Try stopping and restarting Ollama

**Quick Fix**: Open a new terminal and run:
```bash
ollama serve
```"""
            
    except Exception as e:
        return f"❌ **Unexpected Error**: {str(e)}\n\nPlease check the console for more details."

def generate_basic_insights(df):
    """Generate basic statistical insights without AI"""
    try:
        insights = []
        
        # Basic dataset info
        insights.append(f"## 📊 **Dataset Overview**")
        insights.append(f"- **Shape**: {df.shape[0]} rows × {df.shape[1]} columns")
        insights.append(f"- **Memory Usage**: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
        insights.append(f"- **Total Missing Values**: {df.isnull().sum().sum()}")
        
        # Data types analysis
        insights.append(f"\n## 📝 **Data Types Analysis**")
        dtype_counts = df.dtypes.value_counts()
        for dtype, count in dtype_counts.items():
            insights.append(f"- **{dtype}**: {count} columns")
        
        # Missing values analysis
        missing_data = df.isnull().sum()
        missing_data = missing_data[missing_data > 0]
        if len(missing_data) > 0:
            insights.append(f"\n## ❓ **Missing Values Analysis**")
            insights.append("Columns with missing values:")
            for col, missing_count in missing_data.items():
                percentage = (missing_count / len(df)) * 100
                insights.append(f"- **{col}**: {missing_count} missing ({percentage:.1f}%)")
        else:
            insights.append(f"\n## ✅ **Data Quality**")
            insights.append("No missing values found in the dataset!")
        
        # Numeric columns analysis
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            insights.append(f"\n## 🔢 **Numeric Columns Analysis**")
            insights.append(f"Found {len(numeric_cols)} numeric columns:")
            for col in numeric_cols:
                col_data = df[col].dropna()
                if len(col_data) > 0:
                    insights.append(f"- **{col}**:")
                    insights.append(f"  - Mean: {col_data.mean():.2f}")
                    insights.append(f"  - Median: {col_data.median():.2f}")
                    insights.append(f"  - Std: {col_data.std():.2f}")
                    insights.append(f"  - Range: {col_data.min():.2f} to {col_data.max():.2f}")
        
        # Categorical columns analysis
        categorical_cols = df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            insights.append(f"\n## 📋 **Categorical Columns Analysis**")
            insights.append(f"Found {len(categorical_cols)} categorical columns:")
            for col in categorical_cols:
                value_counts = df[col].value_counts()
                insights.append(f"- **{col}**: {len(value_counts)} unique values")
                if len(value_counts) <= 10:
                    insights.append(f"  - Top values: {', '.join([f'{k} ({v})' for k, v in value_counts.head(3).items()])}")
        
        # Correlation analysis for numeric columns
        if len(numeric_cols) > 1:
            insights.append(f"\n## 🔗 **Correlation Analysis**")
            correlation_matrix = df[numeric_cols].corr()
            # Find strongest correlations
            correlations = []
            for i in range(len(correlation_matrix.columns)):
                for j in range(i+1, len(correlation_matrix.columns)):
                    corr_value = correlation_matrix.iloc[i, j]
                    if abs(corr_value) > 0.5:  # Only show strong correlations
                        col1 = correlation_matrix.columns[i]
                        col2 = correlation_matrix.columns[j]
                        correlations.append((col1, col2, corr_value))
            
            if correlations:
                insights.append("Strong correlations found:")
                for col1, col2, corr_value in sorted(correlations, key=lambda x: abs(x[2]), reverse=True):
                    insights.append(f"- **{col1}** ↔ **{col2}**: {corr_value:.3f}")
            else:
                insights.append("No strong correlations found between numeric columns.")
        
        # Recommendations
        insights.append(f"\n## 💡 **Recommendations**")
        insights.append("Based on this analysis, consider:")
        
        if len(missing_data) > 0:
            insights.append("- **Data Cleaning**: Address missing values using appropriate strategies")
        
        if len(numeric_cols) > 1:
            insights.append("- **Correlation Analysis**: Explore relationships between numeric variables")
        
        if len(categorical_cols) > 0:
            insights.append("- **Categorical Analysis**: Investigate patterns in categorical variables")
        
        insights.append("- **Visualization**: Create plots to better understand data distributions")
        insights.append("- **Feature Engineering**: Consider creating new features from existing data")
        
        return "\n".join(insights)
        
    except Exception as e:
        return f"❌ Error generating basic insights: {str(e)}"

# Main app
def main():
    st.title("🔥 EDA-GenAI Dashboard")
    st.markdown("*by Mubasshir Ahmed*")
    st.markdown("---")
    
    # Sidebar
    st.sidebar.header("📁 Data Upload")
    
    uploaded_file = st.sidebar.file_uploader(
        "Upload your CSV file",
        type=['csv'],
        help="Upload a CSV file or use the default Titanic dataset"
    )
    
    # Load data
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.data = df
            st.sidebar.success("✅ File uploaded successfully!")
        except Exception as e:
            st.sidebar.error(f"❌ Error reading file: {str(e)}")
            df = load_default_data()
            st.session_state.data = df
    else:
        df = load_default_data()
        st.session_state.data = df
        st.sidebar.info("📊 Using default Titanic dataset")
    
    # Data cleaning options
    st.sidebar.header("🧹 Data Cleaning")
    
    numeric_strategy = st.sidebar.selectbox(
        "Numeric Missing Values:",
        ["mean", "median", "zero"],
        help="Choose how to handle missing numeric values"
    )
    
    categorical_strategy = st.sidebar.selectbox(
        "Categorical Missing Values:",
        ["mode", "unknown"],
        help="Choose how to handle missing categorical values"
    )
    
    if st.sidebar.button("🔄 Clean Data"):
        with st.spinner("Cleaning data..."):
            cleaned_df = clean_data(df, numeric_strategy, categorical_strategy)
            st.session_state.cleaned_data = cleaned_df
            st.success("✅ Data cleaned successfully!")
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Data Overview", "📈 Visualizations", "🤖 AI Insights", "📄 Reports"])
    
    with tab1:
        st.header("📊 Data Overview")
        
        if st.session_state.get('cleaned_data') is not None:
            df_display = st.session_state.cleaned_data
        else:
            df_display = df
        
        # Dataset info
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Rows", df_display.shape[0])
        with col2:
            st.metric("Columns", df_display.shape[1])
        with col3:
            st.metric("Missing Values", df_display.isnull().sum().sum())
        with col4:
            st.metric("Memory Usage", f"{df_display.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        # Data preview
        st.subheader("📋 Data Preview")
        st.dataframe(df_display.head(10), use_container_width=True)
        
        # Data types and missing values
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📝 Data Types")
            dtype_df = pd.DataFrame({
                'Column': df_display.columns,
                'Data Type': [str(dtype) for dtype in df_display.dtypes.values]
            })
            st.dataframe(dtype_df, use_container_width=True)
        
        with col2:
            st.subheader("❓ Missing Values")
            missing_df = pd.DataFrame({
                'Column': df_display.columns,
                'Missing Count': df_display.isnull().sum().values,
                'Missing %': (df_display.isnull().sum() / len(df_display) * 100).values
            })
            st.dataframe(missing_df, use_container_width=True)
        
        # Download cleaned data
        if st.session_state.get('cleaned_data') is not None:
            csv = st.session_state.cleaned_data.to_csv(index=False)
            st.download_button(
                label="📥 Download Cleaned Data (CSV)",
                data=csv,
                file_name=f"cleaned_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    
    with tab2:
        st.header("📈 Visualizations")
        
        if st.session_state.get('cleaned_data') is not None:
            df_viz = st.session_state.cleaned_data
        else:
            df_viz = df
        
        # Create a better layout with proper spacing
        st.markdown("---")
        
        # Plot controls in a more organized layout
        st.subheader("🎨 Plot Configuration")
        
        # First row: Plot type and generate button
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            plot_type = st.selectbox(
                "**Select Plot Type:**",
                ["Distribution Plot", "Boxplot", "Countplot", "Barplot", "Correlation Heatmap"],
                help="Choose the type of visualization you want to create"
            )
        
        with col2:
            # Column selection based on plot type
            if plot_type in ["Distribution Plot", "Countplot"]:
                x_col = st.selectbox("**Select X Column:**", df_viz.columns, help="Choose the column for the x-axis")
                y_col = None
            elif plot_type in ["Boxplot", "Barplot"]:
                x_col = st.selectbox("**Select X Column:**", df_viz.columns, help="Choose the categorical column")
                numeric_cols = df_viz.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    y_col = st.selectbox("**Select Y Column:**", numeric_cols, help="Choose the numeric column")
                else:
                    y_col = None
                    st.warning("No numeric columns available for this plot type")
            else:  # Correlation Heatmap
                x_col = None
                y_col = None
                st.info("Correlation heatmap will show relationships between all numeric columns")
        
        with col3:
            st.write("")  # Add some spacing
            st.write("")  # Add more spacing
            generate_button = st.button("🎨 Generate Plot", type="primary", use_container_width=True)
        
        # Add some spacing
        st.markdown("---")
        
        # Plot display area
        if generate_button:
            with st.spinner("🎨 Generating beautiful plot..."):
                try:
                    fig = generate_plot(df_viz, plot_type, x_col, y_col)
                    
                    # Display the plot in a centered container
                    st.subheader(f"📊 {plot_type}")
                    
                    # Create a container for the plot with better styling
                    plot_container = st.container()
                    with plot_container:
                        # Display the plot with better sizing
                        st.pyplot(fig, use_container_width=True)
                    
                    # Download section
                    st.markdown("---")
                    col_download1, col_download2 = st.columns(2)
                    
                    with col_download1:
                        # Download plot as PNG
                        buf = io.BytesIO()
                        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight', facecolor='#262730')
                        buf.seek(0)
                        st.download_button(
                            label="📥 Download Plot (PNG)",
                            data=buf.getvalue(),
                            file_name=f"{plot_type.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                            mime="image/png",
                            use_container_width=True
                        )
                    
                    with col_download2:
                        # Download plot as SVG (vector format)
                        buf_svg = io.BytesIO()
                        fig.savefig(buf_svg, format='svg', bbox_inches='tight', facecolor='#262730')
                        buf_svg.seek(0)
                        st.download_button(
                            label="📥 Download Plot (SVG)",
                            data=buf_svg.getvalue(),
                            file_name=f"{plot_type.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.svg",
                            mime="image/svg+xml",
                            use_container_width=True
                        )
                    
                    # Plot information
                    st.markdown("---")
                    st.markdown("**📋 Plot Information:**")
                    info_col1, info_col2, info_col3 = st.columns(3)
                    
                    with info_col1:
                        st.metric("Plot Type", plot_type)
                    with info_col2:
                        if x_col:
                            st.metric("X-Axis", x_col)
                        else:
                            st.metric("X-Axis", "All Numeric Columns")
                    with info_col3:
                        if y_col:
                            st.metric("Y-Axis", y_col)
                        else:
                            st.metric("Y-Axis", "Count/Frequency")
                    
                except Exception as e:
                    st.error(f"❌ Error generating plot: {str(e)}")
                    st.info("💡 Try selecting different columns or plot type")
        else:
            # Show instructions when no plot is generated
            st.info("👆 Configure your plot settings above and click 'Generate Plot' to create a visualization")
            
            # Show sample of available columns
            st.markdown("**📋 Available Columns:**")
            col_info1, col_info2 = st.columns(2)
            
            with col_info1:
                st.markdown("**Numeric Columns:**")
                numeric_cols = df_viz.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    for col in numeric_cols:
                        st.write(f"• {col}")
                else:
                    st.write("No numeric columns found")
            
            with col_info2:
                st.markdown("**Categorical Columns:**")
                categorical_cols = df_viz.select_dtypes(include=['object']).columns
                if len(categorical_cols) > 0:
                    for col in categorical_cols:
                        st.write(f"• {col}")
                else:
                    st.write("No categorical columns found")
    
    with tab3:
        st.header("🤖 AI-Powered Insights")
        
        if st.session_state.cleaned_data is not None:
            df_insights = st.session_state.cleaned_data
        else:
            df_insights = df
        
        # Add a toggle for AI vs Basic insights
        col1, col2 = st.columns([3, 1])
        with col1:
            insight_type = st.radio(
                "Choose Insight Type:",
                ["🤖 AI-Powered (Ollama)", "📊 Basic Analysis"],
                help="AI-powered insights require Ollama to be running"
            )
        
        with col2:
            st.write("")
            generate_button = st.button("🧠 Generate Insights", type="primary")
        
        if generate_button:
            with st.spinner("🤖 Analyzing data..."):
                if insight_type == "🤖 AI-Powered (Ollama)":
                    insights = get_llm_insights(df_insights)
                else:
                    insights = generate_basic_insights(df_insights)
                
                st.markdown("""
                <div class="insight-card">
                    <h3 style="color: #FF6B6B; margin-bottom: 1rem;">📊 Data Insights</h3>
                """, unsafe_allow_html=True)
                
                # Format insights with markdown
                formatted_insights = insights.replace('\n', '\n\n')
                st.markdown(formatted_insights)
                
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("👆 Choose your insight type and click 'Generate Insights' to analyze your dataset!")
            
            # Show Ollama status
            st.markdown("---")
            st.subheader("🔧 Ollama Status")
            
            try:
                # Use ollama library to check status
                models = ollama.list()
                if models and 'models' in models:
                    st.success("✅ Ollama is running and accessible")
                    model_names = [model.get('name', 'Unknown') for model in models['models']]
                    if model_names:
                        st.info(f"📦 Available models: {', '.join(model_names)}")
                    else:
                        st.warning("⚠️ No models found. Run `ollama pull mistral` to install a model.")
                else:
                    st.warning("⚠️ No models found. Run `ollama pull mistral` to install a model.")
            except Exception as e:
                st.error("❌ Ollama is not running or not accessible")
                st.info("💡 To use AI-powered insights, start Ollama with: `ollama serve`")
    
    with tab4:
        st.header("📄 Reports")
        
        if st.session_state.cleaned_data is not None:
            df_report = st.session_state.cleaned_data
        else:
            df_report = df
        
        if st.button("📄 Generate PDF Report"):
            with st.spinner("Generating PDF report..."):
                try:
                    pdf_bytes = generate_pdf_report(df, df_report)
                    st.download_button(
                        label="📥 Download PDF Report",
                        data=pdf_bytes,
                        file_name=f"eda_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                        mime="application/pdf"
                    )
                    st.success("✅ PDF report generated successfully!")
                except Exception as e:
                    st.error(f"❌ Error generating PDF: {str(e)}")
        else:
            st.info("👆 Click the button above to generate a comprehensive PDF report!")
    
    # Beautiful Footer with Developer Info
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 15px; margin: 2rem 0;">
        <h3 style="color: #FF6B6B; margin-bottom: 1rem;">👨‍💻 About the Developer</h3>
        <p style="color: #FAFAFA; font-size: 1.1rem; margin-bottom: 1.5rem;">
            <strong>Mubasshir Ahmed</strong><br>
            🧠 Data & AI Enthusiast | Python • SQL • ML • GenAI • BI Tools<br>
            🎓 BCA Graduate | Ex-Full Stack Dev | Est. 2004 | Proud Memon 🧬 | 📚 Lifelong Learner
        </p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
            <a href="https://github.com/mubasshirahmed-3712" target="_blank" style="text-decoration: none;">
                <button style="background: linear-gradient(135deg, #181717 0%, #333 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                    🐙 GitHub
                </button>
            </a>
            <a href="https://www.linkedin.com/in/mubasshir3712/" target="_blank" style="text-decoration: none;">
                <button style="background: linear-gradient(135deg, #0077B5 0%, #005885 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                    💼 LinkedIn
                </button>
            </a>
            <a href="https://www.instagram.com/badhshah._09" target="_blank" style="text-decoration: none;">
                <button style="background: linear-gradient(135deg, #E4405F 0%, #C13584 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                    📸 Instagram
                </button>
            </a>
            <a href="https://mubasshirsportfolio.vercel.app" target="_blank" style="text-decoration: none;">
                <button style="background: linear-gradient(135deg, #FF6B6B 0%, #FF5252 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                    🌐 Portfolio
                </button>
            </a>
        </div>
        <p style="color: #888; margin-top: 1.5rem; font-size: 0.9rem;">
            Made with ❤️ by Mubasshir Ahmed for the Data Science Community
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 




