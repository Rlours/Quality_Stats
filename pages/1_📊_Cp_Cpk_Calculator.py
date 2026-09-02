import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from calculations.capability import calculate_capability
#from calculations.interpretation import interpret_capability


# ---------------------------------------------------------
# LOCAL ENGINEERING GUIDANCE
# ---------------------------------------------------------
# Set these values according to the applicable customer,
# product, or site requirements.
#
# These are NOT universal acceptance standards.

CAPABILITY_GUIDANCE_THRESHOLD = 1.33
CENTERING_GAP_TOLERANCE = 0.05


# ---------------------------------------------------------
# CAPABILITY STATUS
# ---------------------------------------------------------

def capability_status(
    cpk,
    threshold=CAPABILITY_GUIDANCE_THRESHOLD
):

    if cpk < 1.00:
        return "Insufficient", "🔴"

    elif cpk < threshold:
        return "Marginal", "🟠"

    elif cpk < 1.67:
        return "Capable", "🟢"

    else:
        return "Strong Capability", "🟢"


# ---------------------------------------------------------
# ENGINEERING INTERPRETATION
# ---------------------------------------------------------

def capability_interpretation(
    results,
    capability_threshold=CAPABILITY_GUIDANCE_THRESHOLD
):

    """
    Return conservative, configurable engineering
    guidance for capability results.
    """

    cp = results["cp"]
    cpk = results["cpk"]
    cpu = results["cpu"]
    cpl = results["cpl"]

    # -----------------------------------------------------
    # LIMITING SPECIFICATION SIDE
    # -----------------------------------------------------

    limiting_side = (
        "upper specification side (Cpu)"
        if cpu < cpl
        else "lower specification side (Cpl)"
    )

    # -----------------------------------------------------
    # CENTERING GAP
    # -----------------------------------------------------

    centering_gap = cp - cpk

    relative_gap = (
        centering_gap / cp
        if cp
        else 0.0
    )

    # -----------------------------------------------------
    # POTENTIAL CAPABILITY - Cp
    # -----------------------------------------------------

    if cp >= capability_threshold:

        potential = (
            f"Potential capability: Cp is above the "
            f"configured guidance value of "
            f"{capability_threshold:.2f}; the observed "
            "within-process spread is small relative to "
            "the specification width."
        )

    else:

        potential = (
            f"Potential capability: Cp is below the "
            f"configured guidance value of "
            f"{capability_threshold:.2f}; review process "
            "variation against the applicable requirement."
        )

    # -----------------------------------------------------
    # ACTUAL CAPABILITY - Cpk
    # -----------------------------------------------------

    if cpk >= capability_threshold:

        actual = (
            f"Actual capability: Cpk is above the "
            f"configured guidance value of "
            f"{capability_threshold:.2f}; the current "
            "mean and variation meet this local "
            "screening target."
        )

    else:

        actual = (
            f"Actual capability: Cpk is below the "
            f"configured guidance value of "
            f"{capability_threshold:.2f}; investigate "
            "centering and variation before drawing "
            "a capability conclusion."
        )

    # -----------------------------------------------------
    # PROCESS CENTERING
    # -----------------------------------------------------

    if relative_gap <= CENTERING_GAP_TOLERANCE:

        centering = (
            f"Centering: Cpk is "
            f"{centering_gap:.3f} below Cp "
            f"({relative_gap:.1%}); the process appears "
            "reasonably centered for this dataset."
        )

    else:

        centering = (
            f"Centering: Cpk is "
            f"{centering_gap:.3f} below Cp "
            f"({relative_gap:.1%}); the process mean "
            "is reducing actual capability relative "
            "to its potential."
        )

    # -----------------------------------------------------
    # LIMITING SIDE
    # -----------------------------------------------------

    limiting = (
        f"Limiting side: {limiting_side} is closer "
        "in capability terms "
        f"({min(cpu, cpl):.3f} versus "
        f"{max(cpu, cpl):.3f})."
    )

    return (
        potential,
        actual,
        centering,
        limiting
    )


# =========================================================
# PAGE TITLE
# =========================================================
st.title("📊 Cp / Cpk Calculator")

st.markdown(
    """
    Evaluate **potential capability, actual capability,
    process centering, and specification-side performance**
    using measured process data.
    """
)

st.caption(
    "Quality Engineering Toolkit • Process Capability Analysis"
)


# =========================================================
# 1. PROCESS INPUTS
# =========================================================

st.divider()

st.header("1. Process Inputs")
st.caption(
    "Enter the engineering specification limits and nominal target."
)


col1, col2, col3 = st.columns(3)


with col1:

    lsl = st.number_input(
        "Lower Specification Limit (LSL)",
        value=9.80
    )


with col2:

    target = st.number_input(
        "Target",
        value=10.00
    )


with col3:

    usl = st.number_input(
        "Upper Specification Limit (USL)",
        value=10.20
    )
if lsl >= usl:

    st.error(
        "LSL must be less than USL."
    )

    st.stop()
if not (lsl <= target <= usl):

    st.warning(
        "The target is outside the specification range. "
        "Please verify the engineering specification."
    )


# =========================================================
# 2. MEASUREMENT DATA
# =========================================================

st.divider()

st.header("2. Measurement Data")

st.caption(
    "Enter measured values separated by commas."
)


data_text = st.text_area(

    "Enter measurements separated by commas",

    value=(
        "10.02, 10.05, 9.98, 10.01, 10.03, "
        "9.99, 10.00, 10.04, 9.97, 10.01"
    ),

    help=(
        "Example: 10.02, 10.05, 9.98, 10.01"
    ),
)


# =========================================================
# CALCULATE CAPABILITY
# =========================================================

if st.button(
    "📊 Calculate Capability",
    type="primary",
    use_container_width=True
):

    try:

        # -------------------------------------------------
        # CONVERT INPUT DATA TO NUMBERS
        # -------------------------------------------------

        data = [
            float(value.strip())
            for value in data_text.split(",")
            if value.strip()
        ]


        # -------------------------------------------------
        # CALCULATE Cp / Cpk
        # -------------------------------------------------

        results = calculate_capability(
            data,
            lsl,
            usl
        )


        # =================================================
        # 3. PROCESS RESULTS
        # =================================================

        st.divider()
        st.header("3. Process Results")
        st.caption(
             "Summary statistics and capability indices calculated "
            "from the submitted measurement data."
                )
        


        summary_columns = st.columns(4)


        summary_columns[0].metric(
            "Sample size",
            results["n"]
        )


        summary_columns[1].metric(
            "Mean",
            f'{results["mean"]:.4f}'
        )


        summary_columns[2].metric(
            "Std. deviation",
            f'{results["std_dev"]:.4f}'
        )


        summary_columns[3].metric(
            "Range",
            f'{results["maximum"] - results["minimum"]:.4f}'
        )


        # =================================================
        # CAPABILITY DASHBOARD
        # =================================================

        st.subheader("Capability Dashboard")


        st.caption(
            "Cp describes potential capability from "
            "variation alone; Cpk describes actual "
            "capability after process centering is "
            "considered."
        )


        # -------------------------------------------------
        # Cp / Cpk CARDS
        # -------------------------------------------------

        cp_column, cpk_column = st.columns(2)


        with cp_column:

            with st.container(border=True):

                st.metric(
                    "Cp · Potential capability",
                    f'{results["cp"]:.3f}'
                )

                st.caption(
                    "Capability based on process variation only."
                )


        with cpk_column:

            with st.container(border=True):

                st.metric(
                    "Cpk · Actual capability",
                    f'{results["cpk"]:.3f}'
                )

                st.caption(
                    "Capability considering variation and centering."
                )


        # -------------------------------------------------
        # Cpu / Cpl
        # -------------------------------------------------

        side_columns = st.columns(2)


        side_columns[0].metric(
            "Cpu · Upper-side",
            f'{results["cpu"]:.3f}'
        )


        side_columns[1].metric(
            "Cpl · Lower-side",
            f'{results["cpl"]:.3f}'
        )


        # =================================================
        # D6 — PROCESS CAPABILITY ASSESSMENT
        # =================================================

        st.subheader(
            "📊 Process Capability Assessment"
        )


        status, icon = capability_status(
            results["cpk"]
        )


        assessment_col1, assessment_col2 = st.columns(
            [1, 2]
        )


        with assessment_col1:

            st.metric(
                "Cpk",
                f'{results["cpk"]:.3f}'
            )


        with assessment_col2:

            st.markdown(
                f"### {icon} {status}"
            )

            st.caption(
                f"Current screening threshold: "
                f"{CAPABILITY_GUIDANCE_THRESHOLD:.2f}"
            )


        st.caption(
            "The assessment uses Cpk because Cpk considers "
            "both process variation and process centering. "
            "Cp is shown separately as potential capability."
        )


        # =================================================
        # ENGINEERING INTERPRETATION
        # =================================================
        st.subheader("🔎 Engineering Interpretation")


        st.caption(
            f"Guidance is configurable: this page currently "
            f"uses {CAPABILITY_GUIDANCE_THRESHOLD:.2f} as a "
            "local screening value, not a universal standard."
        )


        potential, actual, centering, limiting = (
            capability_interpretation(results)
        )


        # -------------------------------------------------
        # POTENTIAL CAPABILITY
        # -------------------------------------------------

        if results["cp"] >= CAPABILITY_GUIDANCE_THRESHOLD:

            st.success(potential)

        else:

            st.warning(potential)


        # -------------------------------------------------
        # ACTUAL CAPABILITY
        # -------------------------------------------------

        if results["cpk"] >= CAPABILITY_GUIDANCE_THRESHOLD:

            st.success(actual)

        else:

            st.warning(actual)


        # -------------------------------------------------
        # CENTERING
        # -------------------------------------------------

        centering_gap = (
            (results["cp"] - results["cpk"])
            / results["cp"]
            if results["cp"] != 0
            else 0
        )


        if centering_gap <= CENTERING_GAP_TOLERANCE:

            st.info(centering)

        else:

            st.warning(centering)


        # -------------------------------------------------
        # LIMITING SIDE
        # -------------------------------------------------

        st.info(limiting)


        # =================================================
        # 4. PROCESS CAPABILITY HISTOGRAM
        # =================================================

        st.divider()

        st.header(
            "4. Process Capability Histogram"
        )


        st.caption(
            "Distribution of measurements relative to the "
    "specification limits, target, and process mean."
        )


        fig, ax = plt.subplots(
            figsize=(10, 5)
        )


        # -------------------------------------------------
        # HISTOGRAM
        # -------------------------------------------------

        ax.hist(
            data,
            bins="auto",
            color="#4C78A8",
            edgecolor="white",
            linewidth=1.2,
            alpha=0.9
        )


        # -------------------------------------------------
        # SPECIFICATION LIMITS
        # -------------------------------------------------

        ax.axvline(
            lsl,
            color="#C0392B",
            linestyle="--",
            linewidth=2,
            label=f"LSL ({lsl:.3f})"
        )


        ax.axvline(
            usl,
            color="#C0392B",
            linestyle="--",
            linewidth=2,
            label=f"USL ({usl:.3f})"
        )


        # -------------------------------------------------
        # TARGET
        # -------------------------------------------------

        ax.axvline(
            target,
            color="#2E86C1",
            linestyle=":",
            linewidth=2.2,
            label=f"Target ({target:.3f})"
        )


        # -------------------------------------------------
        # PROCESS MEAN
        # -------------------------------------------------

        ax.axvline(
            results["mean"],
            color="#1E8449",
            linestyle="-",
            linewidth=2.2,
            label=f"Mean ({results['mean']:.3f})"
        )


        # -------------------------------------------------
        # CHART LABELS
        # -------------------------------------------------

        ax.set_xlabel(
            "Measurement"
        )


        ax.set_ylabel(
            "Frequency"
        )


        ax.set_title(
            "Process Measurement Distribution",
            loc="left",
            fontweight="bold"
        )


        ax.grid(
            axis="y",
            alpha=0.25
        )


        ax.spines["top"].set_visible(
            False
        )


        ax.spines["right"].set_visible(
            False
        )


        ax.legend(
            frameon=False,
            ncol=4,
            loc="upper center",
            bbox_to_anchor=(0.5, 1.16)
        )


        fig.tight_layout()


        st.pyplot(
            fig,
            use_container_width=True
        )


        plt.close(fig)
        st.caption(
    "LSL and USL represent engineering specification limits. "
    "The target is the nominal value and the mean represents "
    "the observed process center."
            )

        # =================================================
        # MEASUREMENT DATA
        # =================================================

        st.subheader("Measurement Data")
        st.caption("Values used in the capability calculation.")

        st.dataframe(
            pd.DataFrame(
                {
                    "Measurement": data
                }
            ),
            use_container_width=True
        )


    # =====================================================
    # ERROR HANDLING
    # =====================================================

    except ValueError as error:

        st.error(
            f"Please check your inputs: {error}"
        )