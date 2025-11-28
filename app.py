import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# BASIC PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Competitive Strategy Interactive Companion",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# SMALL HELPERS
# ---------------------------------------------------------
def info_card(title, body):
    with st.container():
        st.markdown(
            f"""
            <div style="border-radius: 12px; padding: 0.8rem 1rem; 
                        border: 1px solid #e0e0e0; background-color: #fafafa;">
                <h4 style="margin-bottom: 0.3rem;">{title}</h4>
                <p style="margin-top: 0.1rem; margin-bottom: 0rem;">{body}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def quiz_question(question, options, correct_index, key_prefix):
    st.write(f"**{question}**")
    answer = st.radio("Choose one:", options, key=key_prefix)
    if "submitted" in st.session_state and st.session_state["submitted"]:
        if options.index(answer) == correct_index:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Not quite – correct answer: **{options[correct_index]}**")

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.title("📚 Competitive Strategy Hub")
st.sidebar.markdown("A tiny ‘course in a box’ to revise the main ideas.")

page = st.sidebar.radio(
    "Jump to section:",
    (
        "Welcome & Course Map",
        "Macro-Environment & PESTEL",
        "Industry Analysis & Five Forces",
        "Value Stick & Generic Strategies",
        "Strategy Clock & Blue Ocean",
        "Competitors, Markets & BSG",
        "Resources, VRIO & RBV",
        "Dynamic Capabilities & Adaptation"
    )
)

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

# Button to reveal quiz feedback on each page
st.sidebar.markdown("---")
if st.sidebar.button("📝 Reveal quiz answers / feedback"):
    st.session_state["submitted"] = True

# ---------------------------------------------------------
# 1. WELCOME PAGE
# ---------------------------------------------------------
if page == "Welcome & Course Map":
    st.title("📊 Competitive Strategy – Interactive Companion")
    st.markdown(
        """
        This app is meant to feel like a tiny “interactive textbook” for the course.  
        Use the sidebar to move through the big blocks:
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧭 Big Questions")
        st.markdown(
            """
            - **Where do we compete?** (industry, segment, geography)  
            - **How do we compete?** (cost vs differentiation, generic strategy)  
            - **With which resources?** (RBV, VRIO, capabilities)  
            - **How do we adapt over time?** (dynamic capabilities)
            """
        )
    with col2:
        st.subheader("🎮 How to use this tool")
        st.markdown(
            """
            - Check the **interactive sliders** to see how value is created and captured.  
            - Use the **quizzes** to test if you really understand the logic.  
            - Think: *‘How would I use this in a real case or in BSG?’*
            """
        )

    st.markdown("---")
    st.subheader("Course Roadmap (mini mental map)")
    cols = st.columns(4)
    with cols[0]:
        info_card(
            "Macro & Industry",
            "PESTEL, scenarios, Five Forces, industry life cycle."
        )
    with cols[1]:
        info_card(
            "Positioning",
            "Value stick, cost vs differentiation, generic strategies."
        )
    with cols[2]:
        info_card(
            "Competitors & Markets",
            "Strategic groups, KSFs, segmentation, Starbucks/BSG."
        )
    with cols[3]:
        info_card(
            "Inside the Firm",
            "Resources, VRIO, core competences, dynamic capabilities."
        )

# ---------------------------------------------------------
# 2. MACRO & PESTEL
# ---------------------------------------------------------
elif page == "Macro-Environment & PESTEL":
    st.title("🌍 Macro-Environment & PESTEL")

    st.markdown(
        """
        The **macro-environment** is the big context outside the industry – politics, 
        economy, society, technology, ecology and law.  
        We use **PESTEL** to structure it and spot **key drivers of change** (the few 
        variables that really force us to rethink strategy).
        """
    )

    st.markdown("### 1. Classify events with PESTEL")
    factor = st.text_input(
        "Type a trend / event (e.g. 'EU carbon tax', 'aging population', 'AI regulation')",
        value="AI regulation in the EU"
    )
    category = st.selectbox(
        "Which PESTEL dimension fits best?",
        ["Political", "Economic", "Sociocultural", "Technological", "Environmental", "Legal"]
    )

    st.write(f"➡️ You classified **'{factor}'** as **{category}**.")
    st.info("Ask yourself: is this a **threat**, an **opportunity**, or both for a specific industry?")

    st.markdown("### 2. Threat or Opportunity? Quick scenario")
    industry = st.selectbox(
        "Pick an industry:",
        ["Oil & Gas", "Fast Fashion", "Plant-based Food", "Low-cost Airlines", "Big Tech Platforms"]
    )
    trend = st.selectbox(
        "Pick a macro trend:",
        [
            "Stricter carbon regulation",
            "Rising interest rates",
            "Gen Z focus on sustainability",
            "Breakthrough in AI automation",
            "Data protection & privacy laws (GDPR-style)"
        ]
    )

    # Very simple illustrative logic
    threat, opportunity = False, False
    explanation = ""
    if trend == "Stricter carbon regulation":
        if industry in ["Oil & Gas", "Low-cost Airlines", "Fast Fashion"]:
            threat, opportunity = True, True
            explanation = "Costs and constraints go up, but also pressure to innovate & differentiate on sustainability."
        else:
            opportunity = True
            explanation = "Creates relative advantage if your product is low-carbon or helps others reduce emissions."
    elif trend == "Gen Z focus on sustainability":
        if industry in ["Fast Fashion", "Oil & Gas"]:
            threat, opportunity = True, True
            explanation = "Legacy models are challenged, but sustainable repositioning can unlock new demand."
        else:
            opportunity = True
            explanation = "You can design offerings that speak directly to these values."
    else:
        explanation = "Impact depends on your business model – think cost of capital, data needs, or regulation risk."

    colT, colO = st.columns(2)
    with colT:
        st.metric("Threat?", "✅" if threat else "⚪")
    with colO:
        st.metric("Opportunity?", "✅" if opportunity else "⚪")

    st.caption(explanation)

    st.markdown("### 3. Quick check – macro vs micro environment")
    quiz_question(
        "A new low-cost airline enters the market. Macro or micro?",
        ["Macro-environment", "Micro / industry environment"],
        correct_index=1,
        key_prefix="q_pe_1"
    )
    quiz_question(
        "A new data privacy law that affects all digital businesses. Macro or micro?",
        ["Macro-environment", "Micro / industry environment"],
        correct_index=0,
        key_prefix="q_pe_2"
    )

# ---------------------------------------------------------
# 3. INDUSTRY ANALYSIS & FIVE FORCES
# ---------------------------------------------------------
elif page == "Industry Analysis & Five Forces":
    st.title("🏭 Industry Analysis & Five Forces")

    st.markdown(
        """
        **Industry analysis** asks: *“Why are some industries systematically more profitable than others?”*  
        The classic tool is **Porter’s Five Forces**, which explains **industry attractiveness**.
        """
    )

    st.markdown("### 1. Explore Five Forces in different industries")
    industry = st.selectbox(
        "Choose an industry:",
        ["Airlines", "Soft Drinks", "Fast Food", "Pharmaceuticals", "Consulting"]
    )

    # Tiny, stylised force levels
    data = {
        "Airlines":          ["High", "High", "High", "High", "Low"],
        "Soft Drinks":       ["Low", "Medium", "Medium", "Medium", "High"],
        "Fast Food":         ["Medium", "Medium", "High", "Medium", "Medium"],
        "Pharmaceuticals":   ["Low", "Medium", "Low", "Medium", "High"],
        "Consulting":        ["Medium", "Low", "Low", "Medium", "Medium"],
    }
    forces = ["Threat of new entrants",
              "Bargaining power of suppliers",
              "Bargaining power of buyers",
              "Threat of substitutes",
              "Rivalry among existing firms"]

    df = pd.DataFrame({"Force": forces, "Intensity": data[industry]})
    st.dataframe(df, hide_index=True)

    st.caption("High intensity = pressure on profits. The more *High* you see, the less attractive the industry.")

    st.markdown("### 2. Industry life cycle intuition")
    stage = st.slider(
        "Where is your chosen industry in its life cycle?",
        1, 4, 3,
        format="%d",
        help="1=Introduction, 2=Growth, 3=Maturity, 4=Decline"
    )

    stage_names = {1: "Introduction", 2: "Growth", 3: "Maturity", 4: "Decline"}
    st.write(f"📈 You selected: **{stage_names[stage]}** stage")

    if stage == 1:
        st.info("Few players, lots of uncertainty, experimentation, low profits but big upside.")
    elif stage == 2:
        st.info("Demand exploding, many entrants, capacity expansion, still good profitability.")
    elif stage == 3:
        st.info("Market saturates; rivalry intensifies; focus on efficiency and differentiation.")
    else:
        st.info("Shrinking demand, excess capacity, price wars, many exits or consolidation.")

    st.markdown("### 3. Quick Five Forces quiz")
    quiz_question(
        "In which industry are **switching costs for consumers** typically LOW?",
        ["Commercial aircraft manufacturing", "Mobile phone operating systems", "Bottled water"],
        correct_index=2,
        key_prefix="q_ff_1"
    )
    quiz_question(
        "If suppliers are few and very specialized, supplier power is usually…",
        ["Low", "Medium", "High"],
        correct_index=2,
        key_prefix="q_ff_2"
    )

# ---------------------------------------------------------
# 4. VALUE STICK & GENERIC STRATEGIES
# ---------------------------------------------------------
elif page == "Value Stick & Generic Strategies":
    st.title("📏 Value Stick & Generic Strategies")

    st.markdown(
        """
        The **value stick** separates total value into four pieces: customer surplus, firm profit, 
        and supplier surplus.  
        Your **competitive advantage** comes from creating more total value *(WTP − SOC)* and/or 
        capturing a bigger slice of it.
        """
    )

    st.markdown("### 1. Play with the value stick")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Set the four ‘points’ on the stick:")
        wts = st.slider("Suppliers’ opportunity cost (WTS / SOC)", 0, 100, 30, step=1)
        cost = st.slider("Your cost (per unit)", wts, 120, 50, step=1)
        price = st.slider("Price you charge", cost, 150, 80, step=1)
        wtp = st.slider("Customer willingness to pay (WTP)", price, 200, 120, step=1)

    with col2:
        customer_surplus = wtp - price
        firm_profit = price - cost
        supplier_surplus = cost - wts
        total_value = wtp - wts

        st.subheader("Decomposition")
        st.metric("Customer surplus", f"{customer_surplus}")
        st.metric("Firm profit", f"{firm_profit}")
        st.metric("Supplier surplus", f"{supplier_surplus}")
        st.metric("Total value created (WTP − WTS)", f"{total_value}")

        chart_df = pd.DataFrame(
            {
                "Component": ["Customer surplus", "Firm profit", "Supplier surplus"],
                "Value": [customer_surplus, firm_profit, supplier_surplus],
            }
        )
        chart_df = chart_df.set_index("Component")
        st.bar_chart(chart_df)

    st.caption("Try lowering cost vs raising WTP and see how it changes value creation and capture.")

    st.markdown("### 2. Generic strategies – where are you on the map?")
    wtp_level = st.selectbox("Relative WTP level vs rivals:", ["Lower", "Similar", "Higher"])
    cost_level = st.selectbox("Relative cost level vs rivals:", ["Lower", "Similar", "Higher"])
    scope = st.selectbox("Scope of target:", ["Broad market", "Niche / focused"])

    if wtp_level == "Higher" and cost_level in ["Similar", "Higher"]:
        base = "Differentiation strategy"
    elif cost_level == "Lower" and wtp_level in ["Similar", "Lower"]:
        base = "Cost leadership strategy"
    elif scope == "Niche / focused" and wtp_level == "Higher":
        base = "Focused differentiation"
    elif scope == "Niche / focused" and cost_level == "Lower":
        base = "Focused low-cost"
    else:
        base = "Potentially stuck in the middle 😬"

    st.success(f"🧭 This looks like: **{base}**")

    st.markdown("### 3. Quick check")
    quiz_question(
        "Southwest Airlines mainly competes through…",
        ["High WTP & high price", "Low cost & low price", "Narrow niche only"],
        correct_index=1,
        key_prefix="q_vs_1"
    )
    quiz_question(
        "A luxury watch brand like Rolex is closest to…",
        ["Cost leadership", "Focused differentiation", "No-frills strategy"],
        correct_index=1,
        key_prefix="q_vs_2"
    )

# ---------------------------------------------------------
# 5. STRATEGY CLOCK & BLUE OCEAN
# ---------------------------------------------------------
elif page == "Strategy Clock & Blue Ocean":
    st.title("⏰ Strategy Clock & Blue Ocean")

    st.markdown(
        """
        The **strategy clock** extends generic strategies by looking at **perceived benefits** 
        vs **price** from the customer’s point of view.  
        **Blue Ocean** thinking asks: *Can we change the ‘rules of the game’ and create an uncontested space?*
        """
    )

    st.markdown("### 1. Choose a position on the strategy clock")
    position = st.selectbox(
        "Which strategic zone are you exploring?",
        [
            "Low price / no-frills",
            "Standard low price",
            "Differentiation (no premium)",
            "Differentiation with premium",
            "Focused differentiation (luxury)",
            "Hybrid (good value for money)"
        ]
    )

    explanations = {
        "Low price / no-frills": "Bare minimum benefits, ultra-low price. Works when customers really only care about price.",
        "Standard low price": "Similar benefits to rivals but lower price – must have a real cost advantage.",
        "Differentiation (no premium)": "Higher benefits at similar price – gain share by offering more for the same money.",
        "Differentiation with premium": "Higher benefits and higher price – margin strategy, brand / quality driven.",
        "Focused differentiation (luxury)": "Extreme benefits, very high price, serving a small segment.",
        "Hybrid (good value for money)": "Above-average benefits at a reasonable cost – often where ‘best cost’ strategies live.",
    }
    st.info(explanations[position])

    st.markdown("### 2. Mini Blue Ocean exercise – redesign an industry value curve")
    st.write("Pick an industry and decide what you would **raise, reduce, create, and eliminate**.")
    bo_industry = st.selectbox(
        "Industry:",
        ["Wine", "Gyms & fitness", "Hotels", "Education", "Airlines"]
    )

    colR, colD = st.columns(2)
    with colR:
        raise_factors = st.text_area("Raise (do more of):", height=80)
        reduce_factors = st.text_area("Reduce (do less of):", height=80)
    with colD:
        create_factors = st.text_area("Create (new factors):", height=80)
        eliminate_factors = st.text_area("Eliminate (remove entirely):", height=80)

    if st.button("🧠 Summarize my Blue Ocean move"):
        st.markdown(
            f"""
            **Your Blue Ocean snapshot for {bo_industry}:**

            - ⬆️ Raise: {raise_factors or '_nothing yet_'}  
            - ⬇️ Reduce: {reduce_factors or '_nothing yet_'}  
            - ✨ Create: {create_factors or '_nothing yet_'}  
            - ❌ Eliminate: {eliminate_factors or '_nothing yet_'}  
            """
        )

    st.markdown("### 3. Quick quiz")
    quiz_question(
        "Blue Ocean strategy focuses mainly on…",
        ["Beating rivals on existing dimensions",
         "Reconstructing market boundaries and unlocking new demand",
         "Copying best practices to reach the productivity frontier"],
        correct_index=1,
        key_prefix="q_bo_1"
    )

# ---------------------------------------------------------
# 6. COMPETITORS, MARKETS & BSG
# ---------------------------------------------------------
elif page == "Competitors, Markets & BSG":
    st.title("🤝 Competitors, Markets & BSG")

    st.markdown(
        """
        Once we know the industry, we zoom in to the **strategic groups** and **segments** where 
        rivalry is strongest and key success factors (KSFs) differ.
        """
    )

    st.markdown("### 1. Strategic group map (toy example for airlines)")
    st.write("Select-up: service level | Sideways: price level")
    airlines = pd.DataFrame(
        {
            "Airline": ["UltraLow", "Ryanair", "EasyJet", "Iberia", "Lufthansa", "Singapore"],
            "Price_level": [1, 2, 2, 3, 4, 5],
            "Service_level": [1, 2, 3, 3, 4, 5],
            "Type": ["ULCC", "Low-cost", "Low-cost", "Legacy", "Legacy", "Premium"]
        }
    )

    st.scatter_chart(
        airlines,
        x="Price_level",
        y="Service_level",
        size=None,
        color="Type"
    )
    st.caption("Strategic groups form where firms have similar combinations of price and service level.")

    st.markdown("### 2. Define a segment & KSFs (think Starbucks in China / BSG)")
    segment_name = st.text_input("Name of segment", value="Urban young professionals")
    ksfs = st.multiselect(
        "Select key success factors for this segment:",
        [
            "Brand & lifestyle fit",
            "Physical convenience / locations",
            "Digital channels & loyalty app",
            "Price sensitivity",
            "Product customization",
            "Local adaptation",
            "Operational efficiency",
        ],
        default=["Brand & lifestyle fit", "Physical convenience / locations", "Digital channels & loyalty app"]
    )

    st.markdown(
        f"""
        For **{segment_name}**, your chosen KSFs are:
        - {", ".join(ksfs) if ksfs else "_none yet_"}
        """
    )

    st.markdown("### 3. Quick BSG-style question")
    quiz_question(
        "If your BSG company wants to move from low image to high image in North America, which **two** levers matter most?",
        [
            "S/Q rating & marketing spend",
            "Inventory levels & base wages",
            "Plant capacity & shipments by region"
        ],
        correct_index=0,
        key_prefix="q_bsg_1"
    )

# ---------------------------------------------------------
# 7. RESOURCES, VRIO & RBV
# ---------------------------------------------------------
elif page == "Resources, VRIO & RBV":
    st.title("🏛️ Resources, VRIO & RBV")

    st.markdown(
        """
        The **Resource-based View (RBV)** starts from the inside:  
        *What is our firm uniquely good at?*  

        - **Resources** = what we have  
        - **Capabilities** = what we can do with what we have  
        - **VRIO** helps decide which ones can support **sustained competitive advantage**.
        """
    )

    st.markdown("### 1. Classify resources")
    res_type = st.selectbox(
        "Pick a resource example:",
        [
            "Cash reserves",
            "Strong brand reputation",
            "Proprietary algorithm",
            "Company culture of experimentation",
            "Standard office building"
        ]
    )

    if res_type == "Cash reserves":
        st.info("Tangible, valuable, but usually not rare or inimitable. Necessary, but rarely a source of sustained advantage alone.")
    elif res_type == "Strong brand reputation":
        st.info("Intangible, often valuable, rare, and harder to copy. A good candidate for VRIO-based advantage.")
    elif res_type == "Proprietary algorithm":
        st.info("Technological, intangible. If protected and hard to imitate, it can be a strong VRIO resource.")
    elif res_type == "Company culture of experimentation":
        st.info("Deeply embedded, intangible. Very hard to copy – classic example of a capability behind sustained advantage.")
    else:
        st.info("Basic tangible resource. Easy to copy and usually not a source of sustained advantage.")

    st.markdown("### 2. VRIO mini-evaluator")
    st.write("For a chosen resource, tick what applies:")
    valuable = st.checkbox("Valuable (helps exploit opportunities / neutralize threats)", key="vrio_v")
    rare = st.checkbox("Rare (few competitors have it)", key="vrio_r")
    hard_to_imitate = st.checkbox("Costly to imitate (or non-substitutable)", key="vrio_i")
    organized = st.checkbox("Organized (firm is structured to capture value from it)", key="vrio_o")

    if st.button("Evaluate VRIO"):
        if not valuable:
            st.error("➡️ Competitive disadvantage or at best wasted resource.")
        elif valuable and not rare:
            st.warning("➡️ Competitive parity – useful, but others have it too.")
        elif valuable and rare and not hard_to_imitate:
            st.info("➡️ Temporary competitive advantage – enjoy it while it lasts.")
        elif valuable and rare and hard_to_imitate and not organized:
            st.warning("➡️ Missed opportunity – you have a potential advantage but are not organized to exploit it.")
        else:
            st.success("🏆 Sustained competitive advantage – VRIO satisfied!")

    st.markdown("### 3. Quick RBV quiz")
    quiz_question(
        "According to RBV, firm performance differences mainly come from…",
        ["Industry structure only", "Unique bundles of resources & capabilities", "Random luck"],
        correct_index=1,
        key_prefix="q_rbv_1"
    )

# ---------------------------------------------------------
# 8. DYNAMIC CAPABILITIES & ADAPTATION
# ---------------------------------------------------------
elif page == "Dynamic Capabilities & Adaptation":
    st.title("🔄 Dynamic Capabilities & Adaptation")

    st.markdown(
        """
        In turbulent environments, it’s not enough to have strong resources today –  
        you need **dynamic capabilities**: the ability to **sense**, **seize**, and **reconfigure**.
        """
    )

    st.markdown("### 1. Tag actions as Sensing, Seizing or Reconfiguring")
    action = st.selectbox(
        "Pick an action:",
        [
            "Launch an internal market scanning unit for AI trends",
            "Invest heavily in a new subscription-based product",
            "Shut down a legacy division and retrain employees",
            "Run surveys to understand changing customer needs"
        ]
    )

    user_tag = st.radio(
        "This is mostly…",
        ["Sensing", "Seizing", "Reconfiguring"],
        key="dc_tag"
    )

    if "submitted" in st.session_state and st.session_state["submitted"]:
        correct_map = {
            "Launch an internal market scanning unit for AI trends": "Sensing",
            "Invest heavily in a new subscription-based product": "Seizing",
            "Shut down a legacy division and retrain employees": "Reconfiguring",
            "Run surveys to understand changing customer needs": "Sensing",
        }
        if user_tag == correct_map[action]:
            st.success("✅ Yes!")
        else:
            st.error(f"❌ More like **{correct_map[action]}** in the Teece framework.")

    st.markdown("### 2. Your adaptation storyline")
    st.write("Imagine a firm facing disruption (e.g., streaming vs DVDs, EVs vs combustion engines).")
    sensing_text = st.text_area("1️⃣ How do they **sense** the change?", height=80)
    seizing_text = st.text_area("2️⃣ How do they **seize** the opportunity?", height=80)
    reconfig_text = st.text_area("3️⃣ How do they **reconfigure** their assets/capabilities?", height=80)

    if st.button("📖 Build my adaptation story"):
        st.markdown(
            f"""
            **Dynamic capabilities in action:**

            - 👀 *Sensing:* {sensing_text or '_not written yet_'}  
            - 🎯 *Seizing:* {seizing_text or '_not written yet_'}  
            - 🛠 *Reconfiguring:* {reconfig_text or '_not written yet_'}  
            """
        )

    st.markdown("### 3. Final check")
    quiz_question(
        "Dynamic capabilities are about…",
        [
            "Operational efficiency in stable environments only",
            "One-time strategic decisions that never change",
            "Routines for renewing and reconfiguring resources over time"
        ],
        correct_index=2,
        key_prefix="q_dc_1"
    )
