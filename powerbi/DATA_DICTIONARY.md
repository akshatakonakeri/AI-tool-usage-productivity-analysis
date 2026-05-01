# Data Dictionary for Power BI

## fact_productivity
- `date`: activity date
- `employee_id`: employee identifier
- `team`: team name
- `role`: role (Developer/Tester/etc.)
- `project`: project name
- `complexity`: task complexity category
- `task_hours`: effort hours for tasks
- `tasks_completed`: count of tasks completed
- `commits`: commit count
- `prs_opened`: pull request count
- `features_delivered`: features delivered
- `test_cases_written`: test cases created
- `ai_usage_events`: AI interaction count
- `hourly_cost`: loaded labor cost per hour
- `period`: `pre_ai` or `post_ai`
- `year_month`: month grain for trends
- `ai_usage_level`: Low/Medium/High usage band

## fact_quality
- `date`: defect record date
- `team`: team name
- `project`: project name
- `defects_total`: total defects
- `defects_sev1`: critical defects
- `reopen_count`: reopened defect count
- `rework_hours`: hours spent in rework
- `period`: `pre_ai` or `post_ai`
- `year_month`: month grain for trends

## fact_costs
- `date`: cost date
- `employee_id`: employee identifier
- `role`: role name
- `hourly_cost`: loaded labor cost
- `ai_license_cost_allocated`: allocated AI licensing cost
- `training_cost_allocated`: allocated training/onboarding cost
- `period`: `pre_ai` or `post_ai`
- `year_month`: month grain for trends

## fact_stats_results
- `metric_name`: metric under test/correlation
- `group`: analysis group, currently overall
- `pre_mean`: pre-AI mean value
- `post_mean`: post-AI mean value
- `pct_change`: percentage change for before/after metrics
- `test`: statistical test used
- `p_value`: significance score
- `effect_size`: effect size or correlation value

## kpi_summary
- `kpi_name`: business KPI label
- `value`: KPI value

## roi_summary
- `metric`: ROI metric label
- `value`: metric value
