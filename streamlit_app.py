
facts = full.get("facts") or {}

if facts:
    with st.expander("What we found"):
        st.json(facts)

    # Surface diagnosis and video brief information when available.
    diag = facts.get("diagnosis") or {}
    sel = facts.get("product_selection") or {}
    brief = facts.get("video_brief") or {}
    qc = facts.get("quality_control") or {}

    if diag or sel or brief:
        with st.expander("Video diagnosis & brief", expanded=False):
            if diag:
                st.subheader("Diagnosis")
                st.json(diag)

            if sel:
                st.subheader("Selected product & score")
                st.json(sel)

            if brief:
                st.subheader("Video brief")

                video_format = brief.get("format", "")
                objective = brief.get("objective", "")

                st.markdown(f"**Format:** {video_format}")
                st.markdown(f"**Objective:** {objective}")

                scenes = brief.get("scenes") or []
                if scenes:
                    st.markdown("**Scenes:**")
                    for scene in scenes:
                        if isinstance(scene, dict):
                            time_label = scene.get("time", "")
                            visual = scene.get("visual", "")
                            description = scene.get(
                                "description", ""
                            )
                            text = visual or description
                            st.markdown(
                                f"- **{time_label}** {text}"
                            )
                        else:
                            st.markdown(f"- {scene}")

                restrictions = brief.get("restrictions") or []
                if restrictions:
                    st.markdown("**Restrictions:**")
                    for restriction in restrictions:
                        st.markdown(f"- {restriction}")

                if st.button("Show full brief JSON"):
                    st.json(brief)

            if qc:
                st.subheader("Quality control")
                st.json(qc)
