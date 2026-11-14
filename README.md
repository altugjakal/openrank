# openrank
A prestige-agnostic ranking algorithm for educational institutions

## Purpose
Most mainstream educational ranking websites weight prestige and brand awareness higher than most other metrics that matter for first year students. Prestige is usually determined through surveys, acceptance rates and number of publications. Our algorithm determines prestige through awareness-agnostic factors.

## Main features

We came up with different approaches to some already existing metrics:

* We have calculated an appropriate acceptance rate per school using faculty size and application intake. Then we used that to highlight the difference between the optimal and actual acceptance rates.
* We also compared the average graduate salary to the country medians in local salary instead of different institutions.
* We decided to include average student professor ratings to determine the strength of faculty-student connection.

## All Input Factors

Each `University` instance takes the following raw institutional metrics:

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **`name`** | `str` | University name and country identifier (e.g., `"KTH (Sweden)"`). |
| **`rank_my_professor_scores`** | `list[float]` | Sampled student teaching evaluation scores (out of `5.0`). |
| **`number_of_startups`** | `int` | Active spinouts and startups founded by university students, faculty, or alumni. |
| **`number_of_students`** | `int` | Total enrolled student headcount / full-time equivalent (FTE). |
| **`avg_undergrad_publications`** | `float` | Annual affiliate-authored peer-reviewed publications per enrolled student. |
| **`avg_patent_publications`** | `float` | Annual affiliate-invented patent filings per 100 enrolled students (regardless of legal assignee). |
| **`avg_tuition_paid_usd`** | `float` | Average annual net tuition paid by domestic students in USD (after institutional grants). |
| **`open_courses`** | `int` | Number of publicly accessible open courses (e.g., OpenCourseWare). |
| **`video_courses`** | `int` | Number of full open video lecture series published online. |
| **`faculty_size`** | `int` | Total academic and teaching faculty headcount. |
| **`demographic_proportions`** | `list[float]` | Proportional breakdown across student demographic or domicile groups (summing to `1.0`). |
| **`national_avg_salary`** | `float` | National median full-time worker salary (in local currency). |
| **`grad_salary`** | `float` | Median graduate starting salary (in local currency). |
| **`avg_class_size`** | `int` / `float` | Average undergraduate/taught class size. |
| **`yearly_intake`** | `int` | Annual incoming student cohort size. |
| **`acceptance_rate`** | `float` | Actual admissions acceptance rate (`0.0` to `1.0`). |
| **`lat`** *(indev)* | `float` | Campus latitude coordinate (used for peer academic cluster proximity). |
| **`lon`** *(indev)* | `float` | Campus longitude coordinate (used for peer academic cluster proximity). |
