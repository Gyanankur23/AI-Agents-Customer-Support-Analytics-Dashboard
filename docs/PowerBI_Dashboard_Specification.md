# AI Agents Customer Support Dashboard - Power BI Specification

## Document Overview

This document provides the complete specification for the AI Agents Customer Support Analytics Dashboard, including data model, DAX measures, visual configurations, and ZoomCharts setup.

## Dashboard Structure

### Single Page Dashboard

#### Key Performance Indicators (KPIs) - Top Row

| KPI Name | DAX Formula | Format |
|----------|-------------|--------|
| Total Tickets | `COUNTROWS(FactSupportTicketsTable)` | #,##0 |
| Avg Resolution Hours | `DIVIDE(SUM(FactSupportTicketsTable[ResolutionHours]), COUNTROWS(FactSupportTicketsTable))` | #,##0.0 "hrs" |
| CSAT Score | `DIVIDE(SUM(FactSupportTicketsTable[CSATScore]), COUNTROWS(FactSupportTicketsTable[CSATScore]))` | #.0 |
| FCR Rate | `DIVIDE(CALCULATE(COUNTROWS(FactSupportTicketsTable), FactSupportTicketsTable[InitialResolvedFlag] = 1), COUNTROWS(FactSupportTicketsTable), 0)` | 0.0% |
| Total Cost EUR | `SUM(FactSupportTicketsTable[AICostEUR]) + SUM(FactSupportTicketsTable[HumanCostEUR]) + SUM(FactSupportTicketsTable[RepeatCostEUR])` | €#,##0 |
| Avg First Response Minutes | `DIVIDE(SUM(FactSupportTicketsTable[FirstResponseMinutes]), COUNTROWS(FactSupportTicketsTable))` | #,##0.0 "min" |
| Repeat Contact Rate | `DIVIDE(CALCULATE(COUNTROWS(FactSupportTicketsTable), FactSupportTicketsTable[RepeatContactCount7d] > 0), COUNTROWS(FactSupportTicketsTable), 0)` | 0.0% |
| Escalation Rate | `DIVIDE(CALCULATE(COUNTROWS(FactSupportTicketsTable), FactSupportTicketsTable[EscalationReason] <> "Not applicable"), COUNTROWS(FactSupportTicketsTable), 0)` | 0.0% |

#### Visual Configurations

**Visual 1: Resolution Time Trend by Support Path (Line Chart)**
- **Fields:**
  - X-Axis: DimDate[Date]
  - Y-Axis: [Avg Resolution Hours]
  - Legend: DimSupportRoute[SupportPath]
- **Settings:**
  - Title: Resolution Time Trend by Support Path
  - Line Type: Smooth
  - Show Points: Yes
  - Time Granularity: Day
  - Color Palette: Purple/Teal gradient

**Visual 2: FCR Rate by Issue Category (Bar Chart)**
- **Fields:**
  - Axis: DimIssue[IssueCategory]
  - Values: [FCR Rate]
- **Settings:**
  - Title: FCR Rate by Issue Category
  - Bar Type: Clustered
  - Data Labels: Show
  - Sort: Descending by value

**Visual 3: CSAT Distribution by Channel & AI Agent (Pie Chart)**
- **Fields:**
  - Legend: DimSupportRoute[Channel]
  - Values: [Total Tickets]
  - Details: DimSupportRoute[AIAgent]
- **Settings:**
  - Title: CSAT Distribution by Channel & AI Agent
  - Color by: Channel
  - Data Labels: Percentage
  - Tooltip: Channel, AI Agent, Ticket Count, Avg CSAT

**Visual 4: Resolution Hours by AI Agent & Product (Stacked Bar Chart)**
- **Fields:**
  - Axis: DimSupportRoute[AIAgent]
  - Values: [Avg Resolution Hours]
  - Legend: DimProduct[ProductName]
- **Settings:**
  - Title: Resolution Hours by AI Agent & Product
  - Bar Type: Stacked
  - Data Labels: Show
  - Sort: Descending by total

**Visual 5: First Response Time by Product & Issue Category (Matrix)**
- **Fields:**
  - Rows: DimProduct[ProductName]
  - Columns: DimIssue[IssueCategory]
  - Values: [Avg First Response Minutes]
- **Settings:**
  - Title: First Response Time by Product & Issue Category
  - Color Scale: Green to Red gradient
  - Data Labels: Show

**Visual 6: Resolution Hours & CSAT by Issue Category (Combo Chart)**
- **Fields:**
  - Axis: DimIssue[IssueCategory]
  - Column Values: [Avg Resolution Hours]
  - Line Values: [CSAT Score]
- **Settings:**
  - Title: Resolution Hours & CSAT by Issue Category
  - Column Color: Purple
  - Line Color: Teal
  - Data Labels: Show

**Visual 7: Ticket Volume by AI Agent & Support Path (Treemap)**
- **Fields:**
  - Group: DimSupportRoute[SupportPath]
  - Values: [Total Tickets]
  - Category: DimSupportRoute[AIAgent]
- **Settings:**
  - Title: Ticket Volume by AI Agent & Support Path
  - Color by: AI Agent
  - Labels: Support Path + Count

**Visual 8: Ticket Distribution by Customer Tier & Lifecycle (Donut Chart)**
- **Fields:**
  - Legend: DimCustomerProfile[CustomerTier]
  - Values: [Total Tickets]
  - Details: DimCustomerProfile[Lifecycle]
- **Settings:**
  - Title: Ticket Distribution by Customer Tier & Lifecycle
  - Donut Hole Size: 50%
  - Color by: Customer Tier
  - Data Labels: Tier + Percentage
  - Tooltip: Tier, Lifecycle, Ticket Count, Avg CSAT

## Data Model

### Fact Table: FactSupportTicketsTable

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| TicketID | Text | Unique root episode identifier |
| CreatedDate | Date | Date-only creation cohort |
| IssueKey | Whole number | Foreign key to DimIssue |
| ProfileKey | Whole number | Foreign key to DimCustomerProfile |
| ProductKey | Whole number | Foreign key to DimProduct |
| RouteKey | Whole number | Foreign key to DimSupportRoute |
| Complexity | Text | Complexity level: Low, Medium, High |
| Priority | Text | Priority: Normal, High, Urgent |
| InitialResolvedFlag | Whole number | 1 = resolved on first contact, 0 = not |
| RepeatContactCount7d | Whole number | Number of repeat contacts within 7 days |
| CSATScore | Whole number | Customer satisfaction score (1-5) |
| FirstResponseMinutes | Decimal | Time to first response in minutes |
| AIConversationMinutes | Decimal | AI handling time in minutes |
| HumanHandlingMinutes | Decimal | Human handling time in minutes |
| QueueMinutes | Decimal | Time spent in queue in minutes |
| ResolutionHours | Decimal | Total resolution time in hours |
| SLATargetHours | Decimal | SLA target in hours |
| SLAMetFlag | Whole number | 1 = SLA met, 0 = SLA missed |
| AICostEUR | Decimal | AI cost in EUR |
| HumanCostEUR | Decimal | Human cost in EUR |
| RepeatCostEUR | Decimal | Cost of repeat contacts in EUR |
| EscalationReason | Text | Reason for escalation (if any) |
| HandoffBand | Text | Handoff band information |

### Dimension Tables

#### DimDate

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| Date | Date | Full date |
| Year | Integer | Year |
| Quarter | Text | Quarter (Q1, Q2, Q3, Q4) |
| MonthNo | Integer | Month number (1-12) |
| MonthName | Text | Month name |
| YearMonth | Text | Year-month format (YYYY-MM) |
| YearMonthSort | Integer | Sortable year-month (YYYYMM) |

#### DimIssue

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| IssueKey | Whole number | Primary key |
| IssueCategory | Text | Issue category (e.g., Account access, Orders & delivery) |
| IssueSubcategory | Text | Issue subcategory (e.g., Password reset, Order tracking) |
| SupportTeam | Text | Support team responsible |

#### DimCustomerProfile

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| ProfileKey | Whole number | Primary key (profile is a segment combination) |
| Region | Text | Geographic region |
| Country | Text | Country |
| Language | Text | Language |
| CustomerTier | Text | Customer tier (Standard, Plus, Premium) |
| Lifecycle | Text | Lifecycle stage (New, Established, Churned) |

#### DimProduct

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| ProductKey | Whole number | Primary key |
| ProductFamily | Text | Product family (Commerce, Productivity) |
| ProductName | Text | Product name |

#### DimSupportRoute

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| RouteKey | Whole number | Primary key |
| Channel | Text | Channel: Live chat, Email |
| SupportPath | Text | Support path: AI only, AI → human, Human only |
| AIAgent | Text | AI agent name (e.g., Assist AI, No AI) |
| PathColor | Text | Color code for visualization |

## DAX Measures

### Core Measures

```dax
Total Tickets = 
COUNTROWS(FactSupportTicketsTable)

Total Tickets per Route = 
CALCULATE(
    [Total Tickets],
    ALLEXCEPT(DimSupportRoute, DimSupportRoute[RouteKey])
)

Avg Resolution Hours = 
DIVIDE(
    SUM(FactSupportTicketsTable[ResolutionHours]),
    COUNTROWS(FactSupportTicketsTable)
)

Avg First Response Minutes = 
DIVIDE(
    SUM(FactSupportTicketsTable[FirstResponseMinutes]),
    COUNTROWS(FactSupportTicketsTable)
)

CSAT Score = 
DIVIDE(
    SUM(FactSupportTicketsTable[CSATScore]),
    COUNTROWS(FactSupportTicketsTable[CSATScore])
)

FCR Count = 
CALCULATE(
    COUNTROWS(FactSupportTicketsTable),
    FactSupportTicketsTable[InitialResolvedFlag] = 1
)

FCR Rate = 
DIVIDE(
    [FCR Count],
    [Total Tickets],
    0
)

Escalation Count = 
CALCULATE(
    COUNTROWS(FactSupportTicketsTable),
    FactSupportTicketsTable[EscalationReason] <> "Not applicable"
)

Escalation Rate = 
DIVIDE(
    [Escalation Count],
    [Total Tickets],
    0
)

Repeat Contact Count = 
CALCULATE(
    COUNTROWS(FactSupportTicketsTable),
    FactSupportTicketsTable[RepeatContactCount7d] > 0
)

Repeat Contact Rate = 
DIVIDE(
    [Repeat Contact Count],
    [Total Tickets],
    0
)

SLA Met Count = 
CALCULATE(
    COUNTROWS(FactSupportTicketsTable),
    FactSupportTicketsTable[SLAMetFlag] = 1
)

SLA Met Rate = 
DIVIDE(
    [SLA Met Count],
    [Total Tickets],
    0
)

Total AI Cost EUR = 
SUM(FactSupportTicketsTable[AICostEUR])

Total Human Cost EUR = 
SUM(FactSupportTicketsTable[HumanCostEUR])

Total Repeat Cost EUR = 
SUM(FactSupportTicketsTable[RepeatCostEUR])

Total Cost EUR = 
[Total AI Cost EUR] + [Total Human Cost EUR] + [Total Repeat Cost EUR]

Avg AI Handling Minutes = 
DIVIDE(
    SUM(FactSupportTicketsTable[AIConversationMinutes]),
    COUNTROWS(FactSupportTicketsTable)
)

Avg Human Handling Minutes = 
DIVIDE(
    SUM(FactSupportTicketsTable[HumanHandlingMinutes]),
    COUNTROWS(FactSupportTicketsTable)
)

Avg Queue Minutes = 
DIVIDE(
    SUM(FactSupportTicketsTable[QueueMinutes]),
    COUNTROWS(FactSupportTicketsTable)
)
```

### Calculated Columns

```dax
Performance Tier = 
SWITCH(
    TRUE(),
    FactSupportTicketsTable[CSATScore] >= 4.5 && FactSupportTicketsTable[ResolutionHours] <= 0.083, "High",
    FactSupportTicketsTable[CSATScore] >= 3.5 && FactSupportTicketsTable[ResolutionHours] <= 0.167, "Medium",
    ISBLANK(FactSupportTicketsTable[CSATScore]) || ISBLANK(FactSupportTicketsTable[ResolutionHours]), "Unknown",
    "Low"
)

Performance Tier Color = 
SWITCH(
    [Performance Tier],
    "High", "#10B981",
    "Medium", "#F59E0B",
    "Low", "#EF4444",
    "Unknown", "#9CA3AF"
)

Resolution Minutes = 
FactSupportTicketsTable[ResolutionHours] * 60
```

## ZoomCharts Configuration

### Network Graph Settings

```json
{
  "nodeSize": {
    "min": 20,
    "max": 50,
    "field": "Total Tickets per Route"
  },
  "linkThickness": {
    "min": 1,
    "max": 3
  },
  "layout": {
    "type": "force-directed",
    "iterations": 100
  },
  "colors": {
    "field": "Performance Tier",
    "palette": ["#10B981", "#F59E0B", "#EF4444"]
  }
}
```

### Time Series Settings

```json
{
  "lineType": "smooth",
  "showPoints": true,
  "timeGranularity": "day",
  "legend": {
    "position": "top",
    "show": true
  },
  "colors": {
    "palette": ["#8B5CF6", "#14B8A6", "#3B82F6"]
  }
}
```

### Sunburst Settings

```json
{
  "innerRadius": "30%",
  "outerRadius": "90%",
  "sort": "descending",
  "sortField": "Total Tickets",
  "colors": {
    "palette": ["#8B5CF6", "#14B8A6", "#F59E0B", "#EF4444"]
  }
}
```

## Slicer Configuration

### Date Range Slicer
- Type: Date Range
- Field: DimDate[Date]
- Default: Last 30 days

### Support Path Slicer
- Type: Checkbox
- Field: DimSupportRoute[SupportPath]
- Default: All selected

### Issue Category Slicer
- Type: Checkbox
- Field: DimIssue[IssueCategory]
- Default: All selected

### AI Agent Slicer
- Type: Checkbox
- Field: DimSupportRoute[AIAgent]
- Default: All selected

### Customer Tier Slicer
- Type: Checkbox
- Field: DimCustomerProfile[CustomerTier]
- Default: All selected

## Bookmark Configuration

### Bookmark 1: High Performers
- Filters: Performance Tier = "High"
- Display: Highlight high-performing tickets

### Bookmark 2: Needs Improvement
- Filters: Performance Tier = "Low"
- Display: Highlight tickets needing attention

### Bookmark 3: High Volume
- Sort: Total Tickets (descending)
- Display: Focus on high-volume support routes

## Tooltips Configuration

### Ticket Performance Tooltip
- Ticket ID
- Support Path
- AI Agent
- Total Tickets
- Avg Resolution Hours
- CSAT Score
- FCR Rate
- Performance Tier

### Ticket Detail Tooltip
- Ticket ID
- Issue Category
- Issue Subcategory
- Resolution Hours
- CSAT Score
- Escalation Reason
- SLA Met (Yes/No)

## Conditional Formatting

### Performance Tier Color Scale
- High: Green (#10B981)
- Medium: Amber (#F59E0B)
- Low: Red (#EF4444)

### CSAT Score Color Scale
- 4.5-5.0: Green (#10B981)
- 3.5-4.4: Amber (#F59E0B)
- Below 3.5: Red (#EF4444)

### Resolution Time Color Scale
- Below 5 hours: Green (#10B981)
- 5-10 hours: Amber (#F59E0B)
- Above 10 hours: Red (#EF4444)

## Data Refresh Configuration

### Refresh Schedule
- Frequency: Daily
- Time: 6:00 AM UTC
- Incremental Refresh: Enabled (last 30 days)

### Gateway Configuration
- Gateway: On-premises data gateway
- Credential: Service account with Excel file access
- Connection: Excel file path

## Security Configuration

### Row-Level Security (RLS)
- Role: Regional Manager
  - Filter: DimCustomerProfile[Region] = USERPRINCIPALNAME()

- Role: Support Team Lead
  - Filter: DimIssue[SupportTeam] = "Team Name"

### Object-Level Security
- Hide sensitive columns: TicketID, ProfileKey
- Show only aggregated metrics to certain roles

## Performance Optimization

### Data Model Optimizations
- Set date table as Mark as Date Table
- Create relationships with single direction
- Use integer keys for relationships
- Disable auto date/time

### Measure Optimizations
- Use CALCULATE with proper filter context
- Avoid iterating over large tables
- Use variables for complex calculations
- Implement DIVIDE with alternative value

## Mobile Layout

### Portrait Mode
- Stack KPIs vertically
- Use tabbed navigation for visuals
- Simplify slicers to dropdowns

### Landscape Mode
- 2x2 grid for KPIs
- Horizontal scroll for visuals
- Compact slicer panel
