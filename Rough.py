import streamlit as st
import re
import random

st.set_page_config(page_title="🔐 PassHub", page_icon="🔐")

st.title("🔐 PassHub")
st.markdown("""## Welcome to ultimate Password Hub! 🔑 
Use this tool to generate strong passwords, check password strength, and verify against common passwords database.""")

# Create tabs for different functions
tab1, tab2 = st.tabs(["🔍 Check Password", "⚙️ Generate Password"])

with tab1:
    st.markdown("### Check your password security")


    # Common password checker
    def check_common_password(user_password):
        with open("common_passwords.txt", 'r', encoding='utf-8') as f:
            common_passwords = f.read().splitlines()

        for i, common_password in enumerate(common_passwords, start=1):
            if user_password.lower() == common_password:
                st.write(f"{user_password} ❌ it is #{i}th Common Password!")
                return

        # This line now runs only AFTER checking all passwords
        st.write(f"{user_password} ✅ It is a Unique Password.")


    user_password = st.text_input("Enter your password", type="password")

    feedback = []
    strength = 0

    if user_password:
        # Check common password first
        check_common_password(user_password)

        if len(user_password) >= 8:
            strength += 1
        else:
            feedback.append("❌ Your password must be 8 characters long!")

        if re.search(r'[A-Z]', user_password) and re.search(r'[a-z]', user_password):
            strength += 1
        else:
            feedback.append("❌ Your password must contain both Uppercase and lowercase characters!")

        if re.search(r'[0-9]', user_password):
            strength += 1
        else:
            feedback.append("❌ Your password must contain at least two digits!")

        if re.search(r'[({!?/\|:;@#$%^&*<>.})]', user_password):
            strength += 1
        else:
            feedback.append("❌ Your password must contain at least one Special character({!?/\|:;@#$%^&*<>.})!")

        if strength == 4:
            feedback.append("✅ Your password is Strong!🎉")
        elif strength == 3:
            feedback.append("🟡 Your password has medium strength. It could be stronger!")
        else:
            feedback.append("🔴 Your password is weak. Please make it stronger!")

        if feedback:
            st.markdown("## Improvements and Suggestions")
            for tips in feedback:
                st.write(tips)

    else:
        st.info("Please enter your password to get started!")

with tab2:
    st.markdown("### 🔑Password Generator⚙️")

    char_set1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_set2 = "abcdefghijklmnopqrstuvwxyz"
    char_set3 = "0123456789"
    char_set4 = "{!?:;@#$%^&*<>.})"  # Fixed: renamed from char_set3 to char_set4

    col1, col2 = st.columns(2)

    with col1:
        length = st.slider("Password length", value=8, max_value=24)

    with col2:
        char_set1 = st.text_input("Uppercase letters", value=char_set1)
        char_set2 = st.text_input("Lowercase letters", value=char_set2)
        char_set3 = st.text_input("Numbers", value=char_set3)
        char_set4 = st.text_input("Special character", value=char_set4)  # Fixed: renamed input variable

    passwords = char_set1 + char_set2 + char_set3 + char_set4


    def generate_password(space, length):
        for _ in range(length):
            yield random.SystemRandom().choice(space)


    if "generated_password" not in st.session_state:
        st.session_state.generated_password = "".join(generate_password(passwords, length))

    if st.button("🔁 Regenerate Password"):
        st.session_state.generated_password = "".join(generate_password(passwords, length))

    col1, col2 = st.columns([3, 1])
    with col1:
        st.info(st.session_state.generated_password)
    with col2:
        st.code(st.session_state.generated_password)

    # Auto-check generated password
    if st.button("🔍 Check This Generated Password"):
        st.markdown("---")
        st.markdown("### Security Analysis of Generated Password")

        st.markdown(
            "Security standards such as NIST recommend a minimum password length of 8 characters, though 12 to 14 characters are often advised for stronger security")

        generated_password = st.session_state.generated_password

        # Check common password
        check_common_password(generated_password)

        # Check strength
        feedback = []
        strength = 0

        if len(generated_password) >= 8:
            strength += 1
        else:
            feedback.append("❌ Your password must be 8 characters long!")

        if re.search(r'[A-Z]', generated_password) and re.search(r'[a-z]', generated_password):
            strength += 1
        else:
            feedback.append("❌ Your password must contain both Uppercase and lowercase characters!")

        if re.search(r'[0-9]', generated_password):
            strength += 1
        else:
            feedback.append("❌ Your password must contain at least one digits!")

        if re.search(r'[({!?:;@#$%^&*<>.})]', generated_password):
            strength += 1
        else:
            feedback.append("❌ Your password must contain at least one Special character({!?:;@#$%^&*<>.})")

        if strength == 4:
            feedback.append("✅ Your password is Strong!🎉")
        elif strength == 3:
            feedback.append("🟡 Your password has medium strength. It could be stronger!")
        else:
            feedback.append("🔴 Your password is weak. Please make it stronger!")

        if feedback:
            st.markdown("## Analysis Results")
            for tips in feedback:
                st.write(tips)
