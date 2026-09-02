def interpret_capability(cp, cpk, cpu, cpl):
    """
    Generate an engineering interpretation of Cp/Cpk results.

    The capability bands below are example engineering
    benchmarks and should be adapted to customer/company
    requirements.
    """

    interpretation = {
        "capability_level": "",
        "capability_message": "",
        "centering_message": "",
        "limiting_side": "",
        "limiting_message": "",
        "conclusion": "",
    }

    # --------------------------------------------------
    # 1. CAPABILITY LEVEL
    # --------------------------------------------------

    if cpk < 1.00:

        capability_level = "Insufficient capability"

        capability_message = (
            f"Cpk = {cpk:.3f}. The observed process variation "
            "and/or process centering do not provide adequate "
            "capability for the selected specification limits."
        )

    elif cpk < 1.33:

        capability_level = "Marginal capability"

        capability_message = (
            f"Cpk = {cpk:.3f}. The process shows limited "
            "capability against the selected specification limits. "
            "Further process improvement may be appropriate."
        )

    elif cpk < 1.67:

        capability_level = "Capable"

        capability_message = (
            f"Cpk = {cpk:.3f}. The process demonstrates "
            "capability against the selected specification limits "
            "based on the selected benchmark."
        )

    else:

        capability_level = "Strong capability"

        capability_message = (
            f"Cpk = {cpk:.3f}. The process demonstrates strong "
            "capability against the selected specification limits "
            "based on the selected benchmark."
        )

    interpretation["capability_level"] = capability_level
    interpretation["capability_message"] = capability_message

    # --------------------------------------------------
    # 2. CENTERING
    # --------------------------------------------------

    if cp == 0:

        centering_difference = 0

    else:

        centering_difference = (cp - cpk) / cp

    if centering_difference <= 0.05:

        centering_message = (
            f"Cp = {cp:.3f} and Cpk = {cpk:.3f}. "
            "The difference between Cp and Cpk is small, "
            "indicating that process centering has relatively "
            "little effect on capability."
        )

    elif centering_difference <= 0.15:

        centering_message = (
            f"Cp = {cp:.3f} and Cpk = {cpk:.3f}. "
            "Cpk is lower than Cp, indicating a moderate "
            "effect of process centering on actual capability."
        )

    else:

        centering_message = (
            f"Cp = {cp:.3f} and Cpk = {cpk:.3f}. "
            "The difference is significant, indicating that "
            "process centering is materially reducing capability."
        )

    interpretation["centering_message"] = centering_message

    # --------------------------------------------------
    # 3. LIMITING SIDE
    # --------------------------------------------------

    if abs(cpu - cpl) < 0.001:

        limiting_side = "Balanced"

        limiting_message = (
            f"Cpu = {cpu:.3f} and Cpl = {cpl:.3f}. "
            "The process has approximately equal capability "
            "relative to both specification limits."
        )

    elif cpu < cpl:

        limiting_side = "Upper specification side"

        limiting_message = (
            f"Cpu = {cpu:.3f} is lower than Cpl = {cpl:.3f}. "
            "The upper specification limit is the limiting side "
            "of the process capability."
        )

    else:

        limiting_side = "Lower specification side"

        limiting_message = (
            f"Cpl = {cpl:.3f} is lower than Cpu = {cpu:.3f}. "
            "The lower specification limit is the limiting side "
            "of the process capability."
        )

    interpretation["limiting_side"] = limiting_side
    interpretation["limiting_message"] = limiting_message

    # --------------------------------------------------
    # 4. OVERALL CONCLUSION
    # --------------------------------------------------

    if cpk < 1.00:

        conclusion = (
            "The process requires improvement. Investigate "
            "process variation, centering and potential special "
            "causes before concluding that the process is capable."
        )

    elif cpk < 1.33:

        conclusion = (
            "The process has limited capability. Consider "
            "reducing variation and/or improving process centering "
            "to increase capability."
        )

    elif cpk < 1.67:

        conclusion = (
            "The process demonstrates capability based on the "
            "selected benchmark. Continue monitoring process "
            "stability and centering."
        )

    else:

        conclusion = (
            "The process demonstrates strong capability based "
            "on the selected benchmark. Continue monitoring "
            "process stability and centering."
        )

    interpretation["conclusion"] = conclusion

    return interpretation