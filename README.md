
```                                       ▄▄     
▄███▄ ████▄ ▄█▀█▄ ████▄ ████▄  ▀▀█▄ ████▄ ██ ▄█▀ 
██ ██ ██ ██ ██▄█▀ ██ ██ ██ ▀▀ ▄█▀██ ██ ██ ████   
▀███▀ ████▀ ▀█▄▄▄ ██ ██ ██    ▀█▄██ ██ ██ ██ ▀█▄  altugnet.org
      ██                                                                                
```

A prestige-agnostic ranking algorithm for educational institutions

## Contributing

Contributions are welcome for adding universities, updating data, or refining the scoring model.

- **Data rules:** Cite official public registries (IPEDS, HESA, UKÄ, Swiss FSO, YÖK Atlas, OpenAlex, CWTS Leiden). Keep salaries in **local currency**, net tuition in **USD** (`0` if tuition-free), and count **affiliate-invented** patents and papers regardless of legal IP title.
- **Algorithm rules:** No reputation surveys or endowment metrics. Keep all scores normalized (`0.0–1.0`) by student or faculty size, and include before/after leaderboard output in PRs that change formulas.
- **Pull requests:** Fork the repo, update `data/universities.csv` or `university.py`, run `python main.py` to verify, and open a PR with your sources.

> We are currently in the process of improving the optimal acceptance rate scoring section; contributions regarding that will be prioritized.

### Guidelines for Adding Universities

When adding a new institution to `data/universities.csv`, follow these standardization rules so cross-country comparisons remain fair:

1. **Cite Primary Registries:** Every value must come from an official public registry, Common Data Set (CDS), institutional annual report, or open bibliometric index (OpenAlex / CWTS Leiden). List your sources per column in the PR description.
2. **Match Scope & Units:**
   - **`number_of_startups`:** Use a **20-year cumulative window** of university spinouts and affiliate-founded startups.
   - **`faculty_size`:** Count teaching-active professorial/academic staff (exclude pure non-teaching research staff).
   - **`avg_tuition_paid_usd`:** Domestic average annual net tuition in **USD** (`0` if statutory tuition-free).
   - **`national_avg_salary` & `grad_salary`:** Enter both in **local currency** (the algorithm uses their ratio, avoiding exchange-rate distortion).
   - **`demographic_proportions`:** Pipe-delimited (`|`) breakdown summing to `1.0`.
   - **`fwci`:** Pull field- and year-normalized citation impact (`1.0` = global field average) from OpenAlex or CWTS Leiden.
   - **Legal-title neutrality:** Count patents and papers produced by university affiliates even in "professor's privilege" (*Lärarundantaget*) countries where individuals hold the patent title.
3. **Verify Locally:** Run `python main.py` after editing `data/universities.csv` to ensure there are no CSV parsing errors and include the resulting terminal output in your PR.

## Purpose
Most mainstream educational ranking websites weight prestige and brand awareness higher than most other metrics that matter for first-year students. Prestige is usually determined through surveys, acceptance rates, and raw publication volume. Our algorithm evaluates institutions through awareness-agnostic factors.

## Main features

We came up with different approaches to some already existing metrics:

- We calculated an appropriate acceptance rate per school using faculty size and application intake, using it to measure the gap between optimal and actual accessibility.
- We compared median graduate starting salary against the national median salary in local currency rather than converting across different economies.
- We included student-professor teaching evaluations and field-weighted citation impact (`fwci`) to measure instructional quality and venue-agnostic research influence.

## All Input Factors

Each `University` instance takes the following raw institutional metrics:

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **`name`** | `str` | University name and country identifier (e.g., `"KTH (Sweden)"`). |
| **`rank_my_professor_scores`** | `list[float]` | Sampled student teaching evaluation scores (out of `5.0`). |
| **`number_of_startups`** | `int` | 20-year cumulative spinouts and startups founded by university students, faculty, or alumni. |
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
| **`fwci`** | `float` | Field-Weighted Citation Impact (`1.0` = global field average; venue-agnostic citation normalization via OpenAlex / CWTS Leiden). |
| **`lat`** *(indev)* | `float` | Campus latitude coordinate (used for peer academic cluster proximity). |
| **`lon`** *(indev)* | `float` | Campus longitude coordinate (used for peer academic cluster proximity). |
