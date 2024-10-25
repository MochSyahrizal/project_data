# Project Data Practicing Basic and Capstone

## Project Background
### Basic Practices
In this project, im practicing basic python, libraries like pandas, matplotlib, seaborn etc. And also practicing new environment of visual studio code, setting extensions and control version system like git and github.

### Capstone Project


## Focus Learn
- Python
- Libraries
- Visual Studio Code
- Git & Github
- Data Cleaning, Analysis & Visualization

## The Analysis (Capstone Project)
### 1. What are the most demanded skills for the top 3 most popular roles?
To find the most demanded skills for the top 3 most popular data roles. I filtered out those positions by which ones were the most popular, and got the top 5 skills for these top 3 roles. This query highlights the most popular job titles and their top skills, showing which skills i should pay attention to depending on the role I'm targetting.

view my notebook with detail steps here:
[2_Skill_Demand.ipynb](2_Capstone_Project\2_Skill_Demand.ipynb)

**Visualize the Data**
```python
fig, ax = plt.subplots(len(job_titles), 1)

sns.set_theme(style='ticks')

for i,  job_title in enumerate(job_titles):
    df_plot = df_skills_perc[df_skills_perc['job_title_short'] == job_title].head(5)
    sns.barplot(data=df_plot, x='skill_percentage', y='job_skills', ax=ax[i], palette='dark:b_r')
    ax[i].set_title(job_title)
    ax[i].set_ylabel('')
    ax[i].set_xlabel('')
    ax[i].get_legend()
    ax[i].set_xlim(0, 78)

    for n, v in enumerate(df_plot['skill_percentage']):
        ax[i].text(v + 1, n, f'{v:.0f}%', va='center')
    
    if i != len(job_titles) - 1 :
        ax[i].set_xticks([])

fig.suptitle('Likelihood Request of Skills in Job Posting', fontsize=15)
fig.tight_layout(h_pad=0.5)
plt.show()
```
**RESULTS**

![2_Capstone_Project\images\skill_demand_all_data_roles.png](https://github.com/MochSyahrizal/project_data/blob/main/2_Capstone_Project/images/skill_demand_all_data_roles.png)


## Insights
- Python is a versatile skill, highly demanded across all three roles, but most prominently for Data Scientists (72%) and Data Engineers (65%).
- SQL is the most requested skill for Data Analysts and Data Scientist, with it in over half the job postings for both roles. For Data Engineers, Python is the most sought-after skill, appearing in 68^ of job postings.
- data Engineer require more specialized technial skill (AWS, Azure, Spark) compared to Data Analysts and Data Scientis who are expected to be proficient in more general data management and analysis tools (Excels, Tableau).
