import streamlit as st


st.set_page_config(
    page_title="Cp / Cpk Theory",
    page_icon="📘",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("📘 Cp / Cpk — Process Capability Theory")

st.write(
    """
    Understand the engineering concepts behind Cp, Cpk,
    Cpu and Cpl, and learn how process variation and
    process centering affect capability.
    """
)


st.divider()


# =========================================================
# 1. WHAT IS PROCESS CAPABILITY?
# =========================================================

st.header("1. What is Process Capability?")


st.write(
    """
    Process capability describes how well the natural
    variation of a process fits within specified engineering
    limits.
    """
)


st.write(
    """
    In simple terms, we are asking:
    """
)


st.info(
    """
    **Can the process consistently produce measurements
    within the specification limits?**
    """
)


st.write(
    """
    Capability indices such as Cp and Cpk compare process
    variation and process centering with the specification
    limits.
    """
)


# =========================================================
# 2. SPECIFICATION LIMITS
# =========================================================

st.header("2. Specification Limits")


st.write(
    """
    A manufacturing characteristic may have an allowable
    specification range.
    """
)


spec_col1, spec_col2, spec_col3 = st.columns(3)


with spec_col1:

    st.metric(
        "LSL",
        "9.80"
    )


with spec_col2:

    st.metric(
        "Target",
        "10.00"
    )


with spec_col3:

    st.metric(
        "USL",
        "10.20"
    )


st.write(
    """
    **LSL** = Lower Specification Limit

    **USL** = Upper Specification Limit

    **Target** = Desired nominal value.
    """
)


st.warning(
    """
    Specification limits are engineering/customer
    requirements. They are not the same thing as
    statistical control limits.
    """
)


# =========================================================
# 3. PROCESS VARIATION
# =========================================================

st.header("3. Process Variation")


st.write(
    """
    No real manufacturing process produces exactly the
    same measurement every time. Measurements naturally
    vary around the process mean.
    """
)


st.write(
    """
    Standard deviation (σ) is commonly used to describe
    the amount of process variation.
    """
)


st.latex(
    r"\sigma = \text{process standard deviation}"
)


st.write(
    """
    Smaller standard deviation means a narrower process
    distribution, while larger standard deviation means
    a wider distribution.
    """
)


# =========================================================
# 4. PROCESS MEAN
# =========================================================

st.header("4. Process Mean")


st.write(
    """
    The process mean represents the average value of the
    measured observations.
    """
)


st.latex(
    r"\bar{x} = \frac{\sum x_i}{n}"
)


st.write(
    """
    The relationship between the process mean and the
    specification limits is important because a process
    can have low variation but still be poorly centered.
    """
)


# =========================================================
# 5. Cp — POTENTIAL CAPABILITY
# =========================================================

st.header("5. Cp — Potential Process Capability")


st.write(
    """
    Cp compares the width of the specification interval
    with approximately six standard deviations of process
    variation.
    """
)


st.latex(
    r"Cp = \frac{USL-LSL}{6\sigma}"
)


st.write(
    """
    Cp considers process variation but does not consider
    where the process mean is located between the
    specification limits.
    """
)


st.info(
    """
    **Cp answers approximately:**

    How large is the specification window compared with
    the natural process spread?
    """
)


# =========================================================
# 6. Cpk — ACTUAL CAPABILITY
# =========================================================

st.header("6. Cpk — Actual Process Capability")


st.write(
    """
    Cpk considers both process variation and process
    centering.
    """
)


st.latex(
    r"Cpk = \min(Cpu,Cpl)"
)


st.write(
    """
    The two one-sided capability indices are:
    """
)


st.latex(
    r"Cpu = \frac{USL-\bar{x}}{3\sigma}"
)


st.latex(
    r"Cpl = \frac{\bar{x}-LSL}{3\sigma}"
)


st.info(
    """
    Cpk is determined by whichever specification side
    is closer in capability terms.
    """
)


# =========================================================
# 7. Cp VS Cpk
# =========================================================

st.header("7. Cp vs Cpk")


comparison = {
    "Feature": [
        "Considers process variation",
        "Considers process centering",
        "Uses specification limits",
        "Potential capability",
        "Actual capability"
    ],

    "Cp": [
        "Yes",
        "No",
        "Yes",
        "Yes",
        "No"
    ],

    "Cpk": [
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes"
    ]
}


st.table(comparison)


# =========================================================
# 8. WHY CAN Cp BE HIGHER THAN Cpk?
# =========================================================

st.header("8. Why Can Cp Be Higher Than Cpk?")


st.write(
    """
    If the process is perfectly centered between the
    specification limits, Cp and Cpk can be close.
    """
)


st.write(
    """
    When the process mean moves toward one specification
    limit, Cpk decreases even if the amount of variation
    has not changed.
    """
)


st.success(
    """
    **Key relationship:**

    When the process is well centered:

    Cp ≈ Cpk
    """
)


st.warning(
    """
    When the process is significantly off-center:

    Cp > Cpk
    """
)


# =========================================================
# 9. CENTERED VS OFF-CENTERED
# =========================================================

st.header("9. Process Centering")


st.subheader("Well-Centered Process")


st.write(
    """
    A centered process has its mean relatively close to
    the target and approximately equal distance from the
    specification limits.
    """
)


st.latex(
    r"Cp \approx Cpk"
)


st.subheader("Off-Centered Process")


st.write(
    """
    When the mean moves toward one specification limit,
    the capability on that side decreases.
    """
)


st.latex(
    r"Cpk < Cp"
)


# =========================================================
# 10. LIMITING SPECIFICATION SIDE
# =========================================================

st.header("10. Limiting Specification Side")


st.write(
    """
    Cpk is the smaller of Cpu and Cpl.
    """
)


st.latex(
    r"Cpk = \min(Cpu,Cpl)"
)


st.write(
    """
    Therefore:
    """
)


st.markdown(
    """
    - If **Cpu < Cpl**, the upper specification side is limiting.
    - If **Cpl < Cpu**, the lower specification side is limiting.
    """
)


# =========================================================
# 11. INTERPRETATION
# =========================================================

st.header("11. Interpreting Capability")


st.write(
    """
    Capability benchmarks depend on the applicable
    customer, product, process and organizational
    requirements.
    """
)


st.warning(
    """
    Values such as 1.33 or 1.67 should not automatically
    be treated as universal acceptance standards.
    Always use the applicable engineering/customer
    requirement.
    """
)


interpretation_table = {
    "Example Cpk range": [
        "< 1.00",
        "1.00 – 1.33",
        "1.33 – 1.67",
        "≥ 1.67"
    ],

    "General screening description": [
        "Potentially insufficient",
        "Marginal",
        "Capable",
        "Strong capability"
    ]
}


st.table(interpretation_table)


# =========================================================
# 12. WORKED EXAMPLE
# =========================================================

st.header("12. Worked Example")


st.write(
    """
    Consider the following example:
    """
)


example_col1, example_col2, example_col3, example_col4 = st.columns(4)


with example_col1:

    st.metric(
        "LSL",
        "9.80"
    )


with example_col2:

    st.metric(
        "USL",
        "10.20"
    )


with example_col3:

    st.metric(
        "Mean",
        "10.010"
    )


with example_col4:

    st.metric(
        "Std. Dev.",
        "0.0258"
    )


st.latex(
    r"Cp = \frac{10.20-9.80}{6(0.0258)}"
)


st.write(
    "Cp ≈ 2.58"
)


st.latex(
    r"Cpu = \frac{10.20-10.010}{3(0.0258)}"
)


st.write(
    "Cpu ≈ 2.45"
)


st.latex(
    r"Cpl = \frac{10.010-9.80}{3(0.0258)}"
)


st.write(
    "Cpl ≈ 2.71"
)


st.latex(
    r"Cpk = \min(2.45,2.71)"
)


st.write(
    "Therefore, Cpk ≈ 2.45."
)


# =========================================================
# 13. IMPORTANT ASSUMPTIONS
# =========================================================

st.header("13. Important Considerations")


st.markdown(
    """
    Before interpreting Cp/Cpk, consider:

    **1. Process stability**

    The process should be reasonably stable before
    capability is meaningfully assessed.

    **2. Measurement system**

    Measurement variation should be appropriate for
    the characteristic being studied.

    **3. Data quality**

    Measurements should be representative of the
    process and collected using an appropriate method.

    **4. Distribution**

    The underlying distribution and assumptions should
    be considered when applying capability indices.

    **5. Specification limits**

    Cp/Cpk compare the process with engineering/customer
    specifications. They do not determine whether the
    specification itself is appropriate.
    """
)


# =========================================================
# 14. COMMON MISTAKES
# =========================================================

st.header("14. Common Mistakes")


mistakes = [
    "Looking only at Cp and ignoring Cpk.",
    "Assuming Cp = Cpk for an off-centered process.",
    "Treating specification limits as control limits.",
    "Using capability indices without considering process stability.",
    "Ignoring measurement-system variation.",
    "Treating a benchmark such as 1.33 as a universal standard.",
    "Concluding that a process is stable simply because Cpk is high."
]


for mistake in mistakes:

    st.markdown(
        f"- {mistake}"
    )


# =========================================================
# 15. Cp/Cpk vs Pp/Ppk
# =========================================================

st.header("15. Cp/Cpk vs Pp/Ppk")


st.write(
    """
    Cp/Cpk and Pp/Ppk are related but are intended to
    describe different aspects of process performance.
    """
)


comparison_pp = {
    "Index": [
        "Cp",
        "Cpk",
        "Pp",
        "Ppk"
    ],

    "General focus": [
        "Potential capability",
        "Capability considering centering",
        "Overall performance",
        "Overall performance considering centering"
    ]
}


st.table(comparison_pp)


st.info(
    """
    A dedicated Pp/Ppk module will be added to the
    Quality Engineering Toolkit in a future version.
    """
)


# =========================================================
# 16. QUICK REFERENCE
# =========================================================

st.header("16. Quick Reference")


st.markdown(
    """
    **Cp**

    Specification width relative to process variation.

    **Cpk**

    Actual capability considering process centering.

    **Cpu**

    Capability relative to the upper specification limit.

    **Cpl**

    Capability relative to the lower specification limit.

    **Mean**

    Average process measurement.

    **Standard deviation**

    Measure of process variation.
    """
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Quality Engineering Toolkit • Cp/Cpk Theory"
)