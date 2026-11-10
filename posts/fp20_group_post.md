# AI Agents Customer Support Analytics Dashboard - Project Submission

## Executive Summary

This project presents a comprehensive Power BI analytics dashboard designed to monitor and optimize AI agent performance in customer support operations. The dashboard provides actionable insights into ticket resolution patterns, customer satisfaction metrics, cost efficiency, and operational effectiveness across multiple support channels and AI agent configurations.

## Technical Architecture

### Data Model
- **Fact Table**: FactSupportTicketsTable (23 columns capturing complete ticket lifecycle)
- **Dimension Tables**: DimDate, DimIssue, DimCustomerProfile, DimProduct, DimSupportRoute
- **Relationships**: Star schema with single-direction cardinality for optimal performance

### Key Performance Indicators
The dashboard tracks eight critical metrics:
- Total Tickets volume
- Average Resolution Hours
- CSAT Score (Customer Satisfaction)
- FCR Rate (First Contact Resolution)
- Total Cost EUR (AI + Human + Repeat costs)
- Average First Response Minutes
- Repeat Contact Rate
- Escalation Rate

### Analytical Visualizations

The single-page dashboard features eight interactive visualizations:

1. **Resolution Time Trend by Support Path** - Temporal analysis of resolution performance across AI-only, AI→human, and human-only support paths
2. **FCR Rate by Issue Category** - Identifies issue types with highest first-contact resolution success
3. **CSAT Distribution by Channel & AI Agent** - Channel performance breakdown (Live Chat, Email) with AI agent attribution
4. **Resolution Hours by AI Agent & Product** - Product-specific performance analysis by AI agent type
5. **First Response Time by Product & Issue Category** - Matrix visualization identifying response time bottlenecks
6. **Resolution Hours & CSAT by Issue Category** - Combo chart correlating resolution time with customer satisfaction
7. **Ticket Volume by AI Agent & Support Path** - Treemap showing workload distribution across support routes
8. **Ticket Distribution by Customer Tier & Lifecycle** - Customer segment analysis for strategic insights

## DAX Implementation

All measures follow Power BI best practices:
- Division operations include alternative values to prevent divide-by-zero errors
- CALCULATE functions use proper filter context management
- Boolean comparisons use TRUE() syntax for DAX compliance
- Performance tier calculations handle NULL values with "Unknown" categorization

## Business Value

This dashboard enables:
- **Operational Optimization**: Identify bottlenecks in resolution times and first response performance
- **Cost Management**: Track AI vs. human cost allocation and repeat contact cost impact
- **Quality Assurance**: Monitor CSAT scores and escalation rates across all support channels
- **Strategic Planning**: Analyze customer segment patterns and product-specific support requirements
- **AI Performance**: Evaluate AI agent effectiveness across different support paths and issue categories

## Technical Considerations

- Date table marked as Date Table for proper time intelligence
- Integer keys used for all relationships to optimize performance
- Auto date/time disabled to prevent model bloat
- Row-level security configured for regional and team-based access control
- Incremental refresh enabled for last 30 days to optimize refresh performance

## Conclusion

This dashboard provides a mature, analytically rigorous foundation for AI-powered customer support operations, enabling data-driven decision-making across operational, financial, and quality dimensions.

---

*Dashboard specifications available in PowerBI_Dashboard_Specification.md*
*Data source: AI_Agents_Customer_Support_Challenge_clean.xlsx*
