import streamlit as st
import pandas as pd
import phq9
import gad7
import database
import followup

database.create_table()

if "generated_assessment" not in st.session_state:
    st.session_state.generated_assessment = None

st.set_page_config(page_title="Mental Health Assessment", page_icon="🧠",
    layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F8FC;
    }.app-header {
    background: white;
    padding: 24px 28px;
    border-radius: 16px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 18px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.05);
}

.header-icon {
    font-size: 42px;
}

.app-header h1 {
    margin: 0;
    font-size: 32px;
}

.app-header p {
    margin: 4px 0 0 0;
    color: #64748B;
    font-size: 16px;
}.disclaimer-card {
    background-color: #EAF2FF;
    border-left: 5px solid #4F8EF7;
    padding: 16px 20px;
    border-radius: 10px;
    margin-bottom: 24px;
    color: #334155;
}

.disclaimer-card strong {
    color: #1E3A5F;
}.result-card {
    background: white;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
    margin-bottom: 20px;
}

.result-label {
    color: #64748B;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 8px;
}

.result-score {
    font-size: 36px;
    font-weight: 700;
    color: #1E293B;
}

.result-score span {
    font-size: 18px;
    color: #94A3B8;
    font-weight: 500;
}

.result-severity {
    margin-top: 8px;
    color: #4F8EF7;
    font-weight: 600;
}.followup-card {
    background-color: #EEF4FF;
    border: 1px solid #D8E6FF;
    border-radius: 14px;
    padding: 20px 22px;
    margin: 8px 0 24px 0;
}

.followup-title {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 6px;
}

.followup-text {
    color: #1E3A5F;
    font-size: 18px;
    font-weight: 600;
}.safety-alert {
    background-color: #FFF1F2;
    border-left: 5px solid #E11D48;
    border-radius: 12px;
    padding: 18px 20px;
    margin-top: 20px;
}

.safety-title {
    color: #9F1239;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 6px;
}

.safety-text {
    color: #881337;
    font-size: 15px;
}.question-text {
    font-size: 16px;
    font-weight: 600;
    color: #1E293B;
    margin-top: 14px;
    margin-bottom: 8px;
}

.question-number {
    display: inline-block;
    color: #4F8EF7;
    font-size: 13px;
    font-weight: 700;
    margin-right: 10px;
}.dashboard-card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 20px 22px;
    min-height: 115px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
}

.dashboard-label {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 10px;
}

.dashboard-value {
    color: #1E293B;
    font-size: 30px;
    font-weight: 700;
}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="app-header">
        <div class="header-icon">🧠</div>
        <div>
            <h1>Mental Health Assessment</h1>
            <p>PHQ-9 & GAD-7 Screening Tool</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="disclaimer-card">
        <strong>Clinical Disclaimer</strong><br>
        This tool is for screening purposes only and does not provide a clinical diagnosis.
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("Patient Information")

patient_col1, patient_col2 = st.columns(2)

with patient_col1:
    patient_id = st.text_input("Patient ID")
    name = st.text_input("Patient Name")

with patient_col2:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )
    doctor = st.selectbox(
        "Doctor",
        ["Dr. A", "Dr. B", "Dr. C"]
    )


response_labels = {
    0: "Not at all",
    1: "Several days",
    2: "More than half the days",
    3: "Nearly every day"
}

def make_response_label(score):
    if score is None:
        return "Select an answer"
    return f"{score} ({response_labels[score]})"

with st.expander("PHQ-9 · Depression Screening", expanded=True):
    st.write(
        "Over the last 2 weeks, how often have you been bothered "
        "by the following problems?"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">01</span>
            Little interest or pleasure in doing things
        </div>
        """,
        unsafe_allow_html=True
    )

    q1 = st.selectbox(
        "PHQ-9 Question 1",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">02</span>
            Feeling down, depressed, or hopeless
        </div>
        """,
        unsafe_allow_html=True
    )

    q2 = st.selectbox(
        "PHQ-9 Question 2",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">03</span>
            Trouble falling or staying asleep, or sleeping too much
        </div>
        """,
        unsafe_allow_html=True
    )

    q3 = st.selectbox(
        "PHQ-9 Question 3",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">04</span>
            Feeling tired or having little energy
        </div>
        """,
        unsafe_allow_html=True
    )

    q4 = st.selectbox(
        "PHQ-9 Question 4",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">05</span>
            Poor appetite or overeating
        </div>
        """,
        unsafe_allow_html=True
    )

    q5 = st.selectbox(
        "PHQ-9 Question 5",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">06</span>
            Feeling bad about yourself, or that you are a failure or have let yourself or your family down
        </div>
        """,
        unsafe_allow_html=True
    )

    q6 = st.selectbox(
        "PHQ-9 Question 6",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">07</span>
            Trouble concentrating on things, such as reading the newspaper or watching television
        </div>
        """,
        unsafe_allow_html=True
    )

    q7 = st.selectbox(
        "PHQ-9 Question 7",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">08</span>
            Moving or speaking so slowly that other people could have noticed? Or the opposite, being so fidgety or restless that you have been moving around a lot more than usual
        </div>
        """,
        unsafe_allow_html=True
    )

    q8 = st.selectbox(
        "PHQ-9 Question 8",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">09</span>
            Thoughts that you would be better off dead or of hurting yourself in some way
        </div>
        """,
        unsafe_allow_html=True
    )

    q9 = st.selectbox(
        "PHQ-9 Question 9",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

phq9_responses = [q1, q2, q3, q4, q5, q6, q7, q8, q9]

with st.expander("GAD-7 · Anxiety Screening", expanded=False):
    st.write(
        "Over the last 2 weeks, how often have you been bothered "
        "by the following problems?"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">01</span>
            Feeling nervous, anxious, or on edge
        </div>
        """,
        unsafe_allow_html=True
    )

    g1 = st.selectbox(
        "GAD-7 Question 1",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">02</span>
            Not being able to stop or control worrying
        </div>
        """,
        unsafe_allow_html=True
    )

    g2 = st.selectbox(
        "GAD-7 Question 2",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">03</span>
            Worrying too much about different things
        </div>
        """,
        unsafe_allow_html=True
    )

    g3 = st.selectbox(
        "GAD-7 Question 3",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">04</span>
            Trouble relaxing
        </div>
        """,
        unsafe_allow_html=True
    )

    g4 = st.selectbox(
        "GAD-7 Question 4",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">05</span>
            Being so restless that it is hard to sit still
        </div>
        """,
        unsafe_allow_html=True
    )

    g5 = st.selectbox(
        "GAD-7 Question 5",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">06</span>
            Becoming easily annoyed or irritable
        </div>
        """,
        unsafe_allow_html=True
    )

    g6 = st.selectbox(
        "GAD-7 Question 6",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="question-text">
            <span class="question-number">07</span>
            Feeling afraid as if something awful might happen
        </div>
        """,
        unsafe_allow_html=True
    )

    g7 = st.selectbox(
        "GAD-7 Question 7",
        [None, 0, 1, 2, 3],
        format_func=make_response_label,
        label_visibility="collapsed"
    )

gad7_responses = [g1, g2, g3, g4, g5, g6, g7]

st.subheader("Assessment Summary")
if st.button("Generate Assessment"):
    if not patient_id.strip():
        st.warning("Please enter the Patient ID.")
    elif not name.strip():
        st.warning("Please enter the patient's name.")
    elif not phq9.is_complete(phq9_responses):
        st.warning("Please answer all PHQ-9 questions.")
    elif not gad7.is_complete(gad7_responses):
        st.warning("Please answer all GAD-7 questions.")
    elif not phq9.is_valid(phq9_responses):
        st.error("Invalid PHQ-9 response.")
    elif not gad7.is_valid(gad7_responses):
        st.error("Invalid GAD-7 response.")
    else:
        phq9_total = phq9.total_score(phq9_responses)
        gad7_total = gad7.total_score(gad7_responses)

        phq9_category = phq9.classify(phq9_total)
        gad7_category = gad7.classify(gad7_total)

        phq9_risk = phq9.check_risk(phq9_responses)

        followup_result = followup.determine_followup(
            phq9_total,
            gad7_total,
            q9
        )

        st.session_state.generated_assessment = {
            "patient_id": patient_id,
            "name": name,
            "age": age,
            "doctor": doctor,
            "phq9_total": phq9_total,
            "gad7_total": gad7_total,
            "phq9_category": phq9_category,
            "gad7_category": gad7_category,
            "item9": q9,
            "followup_result": followup_result
        }

        st.divider()

        st.subheader("Assessment Results")

        st.markdown(
            f"""
            **Patient:** {name}  
            **Patient ID:** {patient_id}  
            **Age:** {age}  
            **Doctor:** {doctor}
            """
        )

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">PHQ-9 · Depression</div>
                    <div class="result-score">{phq9_total}<span> / 27</span></div>
                    <div class="result-severity">{phq9_category}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with result_col2:
            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">GAD-7 · Anxiety</div>
                    <div class="result-score">{gad7_total}<span> / 21</span></div>
                    <div class="result-severity">{gad7_category}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="followup-card">
                <div class="followup-title">Follow-up Recommendation</div>
                <div class="followup-text">{followup_result}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


        if q9 > 0:
            st.markdown(
                """
                <div class="safety-alert">
                    <div class="safety-title">⚠️ Safety Attention Required</div>
                    <div class="safety-text">
                        A non-zero response was recorded for PHQ-9 Item 9.
                        Further safety assessment is recommended.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

if st.session_state.generated_assessment is not None:
    assessment = st.session_state.generated_assessment

    if st.button("Save Assessment"):
        database.save_assessment(
            assessment["patient_id"],
            assessment["name"],
            assessment["age"],
            assessment["doctor"],
            assessment["phq9_total"],
            assessment["gad7_total"],
            assessment["phq9_category"],
            assessment["gad7_category"],
            assessment["item9"],
            assessment["followup_result"]
        )

        st.session_state.generated_assessment = None
        st.success("Assessment saved successfully.")
        st.rerun()

assessments = database.get_assessments()

if assessments:
    df = pd.DataFrame(
        assessments,
        columns=[
            "ID",
            "Patient ID",
            "Name",
            "Age",
            "Doctor",
            "PHQ-9 Score",
            "GAD-7 Score",
            "PHQ-9 Severity",
            "GAD-7 Severity",
            "Item 9 Flag",
            "Follow-up Result",
            "Assessment Date"
        ]
    )

    total_assessments = len(df)
    average_phq9 = round(df["PHQ-9 Score"].mean(), 1)
    average_gad7 = round(df["GAD-7 Score"].mean(), 1)
    followup_required = (
            df["Follow-up Result"] != "Routine screening follow-up"
    ).sum()

    st.subheader("Dashboard")

    dashboard_col1, dashboard_col2, dashboard_col3, dashboard_col4 = st.columns(4)

    with dashboard_col1:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="dashboard-label">Total Assessments</div>
                <div class="dashboard-value">{total_assessments}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with dashboard_col2:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="dashboard-label">Average PHQ-9</div>
                <div class="dashboard-value">{average_phq9}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with dashboard_col3:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="dashboard-label">Average GAD-7</div>
                <div class="dashboard-value">{average_gad7}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with dashboard_col4:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="dashboard-label">Follow-up Required</div>
                <div class="dashboard-value">{followup_required}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    phq9_distribution = df["PHQ-9 Severity"].value_counts()
    gad7_distribution = df["GAD-7 Severity"].value_counts()

    st.subheader("Severity Distribution")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        with st.container(border=True):
            st.markdown("#### PHQ-9 Severity")
            st.caption("Distribution of depression screening severity")
            st.bar_chart(phq9_distribution)

    with chart_col2:
        with st.container(border=True):
            st.markdown("#### GAD-7 Severity")
            st.caption("Distribution of anxiety screening severity")
            st.bar_chart(gad7_distribution)

    st.subheader("Assessment Records")

    doctor_options = ["All"] + list(df["Doctor"].unique())

    selected_doctor = st.selectbox(
        "Filter by Doctor",
        doctor_options
    )

    if selected_doctor == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Doctor"] == selected_doctor]

    st.caption(
        f"Showing {len(filtered_df)} of {len(df)} assessments"
    )

    st.dataframe(
        filtered_df,
        hide_index=True,
        use_container_width=True
    )

    st.subheader("Manage Assessment")

    assessment_options = {
        f"#{row[0]} · {row[1]} - {row[2]}": row
        for row in assessments
    }

    selected_label = st.selectbox(
        "Select a patient",
        list(assessment_options.keys())
    )

    selected = assessment_options[selected_label]

    selected_id = selected[0]
    selected_patient_id = selected[1]
    selected_name = selected[2]
    selected_age = selected[3]
    selected_doctor = selected[4]
    selected_phq9 = selected[5]
    selected_gad7 = selected[6]
    selected_phq9_severity = selected[7]
    selected_gad7_severity = selected[8]
    selected_item9_flag = selected[9]
    selected_followup_result = selected[10]

    manage_col1, manage_col2 = st.columns([2, 1])

    with manage_col1:
        st.write("### Edit Assessment")

        edit_patient_id = st.text_input(
            "Patient ID",
            value=selected_patient_id,
            key=f"patient_id_{selected_id}"
        )

        edit_name = st.text_input(
            "Name",
            value=selected_name,
            key=f"name_{selected_id}"
        )

        edit_age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=max(1, selected_age),
            step=1,
            key=f"age_{selected_id}"
        )

        doctor_options = ["Dr. A", "Dr. B", "Dr. C"]

        edit_doctor = st.selectbox(
            "Doctor",
            doctor_options,
            index=doctor_options.index(selected_doctor),
            key=f"doctor_{selected_id}"
        )

        edit_phq9 = st.number_input(
            "PHQ-9 Score",
            min_value=0,
            max_value=27,
            value=selected_phq9,
            key=f"phq9_{selected_id}"
        )

        edit_gad7 = st.number_input(
            "GAD-7 Score",
            min_value=0,
            max_value=21,
            value=selected_gad7,
            key=f"gad7_{selected_id}"
        )

        edit_item9 = st.number_input(
            "PHQ-9 Item 9 Response",
            min_value=0,
            max_value=3,
            value=selected_item9_flag,
            step=1,
            key=f"item9_{selected_id}"
        )

        if st.button("Update Assessment"):

            if not edit_patient_id.strip():
                st.warning("Please enter the Patient ID.")

            elif not edit_name.strip():
                st.warning("Please enter the patient's name.")

            else:
                edit_phq9_severity = phq9.classify(edit_phq9)
                edit_gad7_severity = gad7.classify(edit_gad7)

                edit_followup_result = followup.determine_followup(
                    edit_phq9,
                    edit_gad7,
                    edit_item9
                )

                database.update_assessment(
                    selected_id,
                    edit_patient_id,
                    edit_name,
                    edit_age,
                    edit_doctor,
                    edit_phq9,
                    edit_gad7,
                    edit_phq9_severity,
                    edit_gad7_severity,
                    edit_item9,
                    edit_followup_result
                )

                st.success("Assessment updated successfully.")
                st.rerun()

    with manage_col2:
        st.write("### Delete Assessment")

        st.warning(
            f"You are about to delete {selected_patient_id} - {selected_name}."
        )

        if st.button(
                "Delete Assessment",
                key=f"delete_{selected_id}"
        ):
            database.delete_assessment(selected_id)
            st.rerun()

else:
    st.info("No assessments saved yet.")