# AI Agents Customer Support Analytics Dashboard

A comprehensive Power BI dashboard for analyzing AI agent performance in customer support operations, tracking efficiency metrics, and identifying optimization opportunities.

## Overview

This dashboard provides real-time visibility into AI agent performance, customer satisfaction metrics, resolution times, and operational efficiency. It enables support teams to make data-driven decisions about AI agent deployment, training needs, and process improvements.

## Dashboard Pages

### Page 1: Agent Performance Overview

Key Performance Indicators:
- Total Interactions Handled
- Average Resolution Time (Minutes)
- Customer Satisfaction Score (CSAT)
- First Contact Resolution Rate

Main Visuals:
- Agent Performance Distribution (ZoomCharts Network Graph)
- Resolution Time Trend (ZoomCharts Time Series)
- Interaction Volume by Category (Treemap)

### Page 2: Detailed Analytics & Insights

Key Performance Indicators:
- Escalation Rate
- Agent Utilization Percentage
- Knowledge Base Coverage
- Average Handling Time (AHT)

Main Visuals:
- Performance by Agent Type (ZoomCharts Sunburst)
- CSAT vs Resolution Time Analysis (Scatter Plot)
- Issue Category Breakdown (Stacked Bar Chart)

## Dashboard Screenshots

### Agent Performance Overview
![Performance Overview](images/performance_overview.png)

### Detailed Analytics & Insights
![Detailed Analytics](images/detailed_analytics.png)

## Key Features

- Interactive slicers for filtering by Date Range, Agent Type, Issue Category, and Performance Tier
- Dynamic performance tier coloring (High/Medium/Low) for quick identification
- ZoomCharts integration for advanced network and time-series visualizations
- Cross-filtering between all visuals for drill-down analysis
- Comprehensive tooltips with interaction details
- Bookmark views for different scenarios (Top Performers, Needs Improvement, High Volume)

## Data Model

### Fact Table
- FactAgentInteractions: Individual interaction records with performance metrics

### Dimension Tables
- DimAgent: AI agent master data
- DimDate: Date calendar
- DimIssueCategory: Issue type categorization
- DimCustomer: Customer information
- DimChannel: Communication channel (chat, email, voice)
- DimPerformanceTier: Performance classification
- DimKnowledgeBase: Knowledge base coverage

## Key Metrics

### Performance Metrics
- Resolution Time (Average, Median, 90th percentile)
- First Contact Resolution Rate
- Customer Satisfaction Score (CSAT)
- Net Promoter Score (NPS)
- Agent Utilization Rate

### Efficiency Metrics
- Average Handling Time (AHT)
- Escalation Rate
- Transfer Rate
- Self-Service Resolution Rate
- Knowledge Base Hit Rate

### Quality Metrics
- Accuracy Score
- Compliance Score
- Training Completion Rate
- Agent Confidence Score

## Technology Stack

- Power BI Desktop
- Power BI Service
- ZoomCharts Custom Visuals (Network Graph, Time Series, Sunburst)
- DAX for calculations and measures

## Installation

### Prerequisites
- Power BI Desktop (latest version)
- Power BI Service account (for publishing and sharing)
- ZoomCharts custom visuals (from AppSource)

### Setup Instructions

1. Clone this repository
2. Download the dataset from the `data/` folder
3. Open the Power BI report file in Power BI Desktop
4. Apply the custom theme: `docs/AI_Agents_Dashboard_Theme.json`
5. Configure data refresh in Power BI Service
6. Publish to your workspace

### Theme Application

To apply the custom theme:
1. Open Power BI Desktop
2. Go to View -> Themes
3. Browse and select `docs/AI_Agents_Dashboard_Theme.json`

## Data Source

The dashboard uses the following Excel file:
- `data/AI_Agents_Customer_Support_Challenge_clean.xlsx`

## DAX Measures

Key measures include:
- Total Interactions
- Average Resolution Time
- CSAT Score
- First Contact Resolution Rate
- Escalation Rate
- Agent Utilization
- Performance Tier (calculated column for conditional formatting)

See `docs/PowerBI_Dashboard_Specification.md` for complete DAX formulas.

## File Structure

```
.
├── AI_Agents_Dashboard.pbix                                    # Power BI report
├── README.md                                                   # This file
├── data/
│   └── AI_Agents_Customer_Support_Challenge_clean.xlsx        # Source data
├── docs/
│   ├── AI_Agents_Dashboard_Theme.json                         # Custom theme
│   └── PowerBI_Dashboard_Specification.md                      # Detailed specs
│   └── What ZoomCharts visuals to use in Power BI.pdf          # ZoomCharts guide
└── images/
    ├── performance_overview.png                                # Overview screenshot
    └── detailed_analytics.png                                  # Analytics screenshot
```

## Usage

### Filtering
Use the slicers on the left sidebar to filter data by:
- Date Range (daily, weekly, monthly)
- Agent Type (Rule-based, ML-based, Hybrid)
- Issue Category (Technical, Billing, General, etc.)
- Performance Tier (High, Medium, Low)

### Navigation
- Use page tabs to switch between Performance Overview and Detailed Analytics
- Click on any visual to cross-filter other visuals
- Use bookmarks for quick access to filtered views

### Drill-down
- Click on issue categories in the treemap to see specific agents
- Click on agent types in the sunburst to see performance details
- Hover over scatter plot points for interaction-specific metrics

## Customization

### Adding New Measures
1. Go to Data view
2. Select the FactAgentInteractions table
3. Click "New Measure" in the ribbon
4. Write your DAX formula
5. Use the measure in visuals

### Modifying Colors
Edit `docs/AI_Agents_Dashboard_Theme.json` to customize:
- Data colors (purple/teal gradient theme)
- Background colors
- Font styles (currently set to bold)
- Visual-specific styling

### Adding New Visuals
Refer to `docs/PowerBI_Dashboard_Specification.md` for:
- Visual type recommendations
- Data field mappings
- ZoomCharts configuration

## Refresh Schedule

Configure scheduled refresh in Power BI Service:
- Dataset refresh: Daily or weekly (depending on data update frequency)
- Gateway setup required for on-premises Excel sources

## Contributors

- Gyanankur Baruah

## License

This project is for educational and demonstration purposes.

## Contact

For questions or feedback, please open an issue in the repository.

## Future Enhancements

- Real-time data integration via API
- Predictive analytics for agent performance
- Automated alert notifications for performance degradation
- Mobile-optimized report layout
- Natural language Q&A integration
- Sentiment analysis integration
