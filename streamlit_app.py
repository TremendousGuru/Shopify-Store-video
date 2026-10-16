@@
     facts = full.get("facts") or {}
     if facts:
-        with st.expander("What we found"):
-            st.json(facts)
+        with st.expander("What we found"):
+            st.json(facts)
+        # Surface the new diagnosis and video brief information, if present.
+        diag = facts.get("diagnosis") or {}
+        sel = facts.get("product_selection") or {}
+        brief = facts.get("video_brief") or {}
+        qc = facts.get("quality_control") or {}
+        if diag or sel or brief:
+            with st.expander("Video diagnosis & brief", expanded=False):
+                if diag:
+                    st.subheader("Diagnosis")
+                    st.json(diag)
+                if sel:
+                    st.subheader("Selected product & score")
+                    st.json(sel)
+                if brief:
+                    st.subheader("Video brief")
+                    # Show a concise brief summary and allow expansion to JSON
+                    st.markdown(f"**Format:** {brief.get('format', '')}  ")
+                    st.markdown(f"**Objective:** {brief.get('objective', '')}\n\n")
+                    if brief.get("scenes"):
+                        st.markdown("**Scenes:**")
+                        for s in brief.get("scenes"):
+                            st.markdown(f"- {s.get('time')}: {s.get('visual')}")
+                    st.markdown("\n**Restrictions:**")
+                    for r in brief.get("restrictions", []):
+                        st.markdown(f"- {r}")
+                    st.button("Show full brief JSON", on_click=lambda: st.json(brief))
