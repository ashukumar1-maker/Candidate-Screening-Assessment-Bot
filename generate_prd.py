from fpdf import FPDF

class PRD(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, "PROVANA INTERNAL  |  CONFIDENTIAL", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(180, 180, 180)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, "Page " + str(self.page_no()) + "  |  Author: ASHU KUMAR (AIML)  |  July 2026  |  PRD v0.1", align="C")

pdf = PRD()
pdf.set_margins(15, 12, 15)
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()

W = pdf.epw


def title_block():
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(15, 35, 80)
    pdf.cell(W, 11, "Candidate Screening & Assessment Bot", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(W, 6, "Product Requirements Document  |  v0.1  |  Draft", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    pdf.cell(W, 6, "Author: ASHU KUMAR (AIML)     Date: July 2026     Status: Discovery", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(9)


def section_header(title):
    pdf.ln(3)
    pdf.set_fill_color(15, 35, 80)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(W, 9, "  " + title, fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)


def para(text):
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(W, 6, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)


def label(text):
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(15, 35, 80)
    pdf.cell(W, 7, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def bullet(items):
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(40, 40, 40)
    for item in items:
        pdf.multi_cell(W, 6, "   -  " + item, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)


def th2(h1, h2):
    C1, C2 = 75, W - 75
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(15, 35, 80)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(C1, 8, "  " + h1, border=1, fill=True)
    pdf.cell(C2, 8, "  " + h2, border=1, fill=True, new_x="LMARGIN", new_y="NEXT")


def row2(c1, c2, shade=False):
    C1, C2 = 75, W - 75
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(40, 40, 40)
    pdf.set_fill_color(238, 243, 255) if shade else pdf.set_fill_color(252, 252, 255)
    # calculate row height based on longer cell
    chars_per_line_c1 = 36
    chars_per_line_c2 = 55
    lines = max(
        max(1, -(-len(c1) // chars_per_line_c1)),
        max(1, -(-len(c2) // chars_per_line_c2))
    )
    h = lines * 6 + 3
    x, y = pdf.get_x(), pdf.get_y()
    pdf.multi_cell(C1, h, "  " + c1, border=1, fill=True, new_x="RIGHT", new_y="TOP")
    pdf.set_xy(x + C1, y)
    pdf.multi_cell(C2, h, "  " + c2, border=1, fill=True, new_x="LMARGIN", new_y="NEXT")


def th3(h1, h2, h3):
    C1, C2, C3 = 10, 112, W - 122
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(15, 35, 80)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(C1, 8, " " + h1, border=1, fill=True)
    pdf.cell(C2, 8, "  " + h2, border=1, fill=True)
    pdf.cell(C3, 8, "  " + h3, border=1, fill=True, new_x="LMARGIN", new_y="NEXT")


def row3(c1, c2, c3, shade=False):
    C1, C2, C3 = 10, 112, W - 122
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(40, 40, 40)
    pdf.set_fill_color(238, 243, 255) if shade else pdf.set_fill_color(252, 252, 255)
    lines = max(
        max(1, -(-len(c2) // 50)),
        max(1, -(-len(c3) // 26))
    )
    h = lines * 6 + 3
    x, y = pdf.get_x(), pdf.get_y()
    pdf.multi_cell(C1, h, " " + c1, border=1, fill=True, new_x="RIGHT", new_y="TOP")
    pdf.set_xy(x + C1, y)
    pdf.multi_cell(C2, h, "  " + c2, border=1, fill=True, new_x="RIGHT", new_y="TOP")
    pdf.set_xy(x + C1 + C2, y)
    pdf.multi_cell(C3, h, "  " + c3, border=1, fill=True, new_x="LMARGIN", new_y="NEXT")


def divider():
    pdf.set_draw_color(200, 210, 230)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(4)


# ── CONTENT ────────────────────────────────────────────────────────────────

title_block()

section_header("Problem Statement")
para(
    "Provana's Talent Acquisition team manually screens resumes and conducts Voice & Aptitude "
    "(V&A) assessments, requiring 3 recruiters and 1 V&A resource. This creates a capacity ceiling, "
    "limits hiring scale, and costs Rs. 51 Lakhs annually. This bot automates screening and "
    "assessment end-to-end, reducing cost and nearly doubling throughput with the same headcount."
)

section_header("Phase 1  -  Resume Screening & Bulk Upload")

label("Scope")
bullet([
    "Bulk resume upload: PDF, Word, Image files, Scanned PDFs",
    "AI-based JD matching and scoring using Claude Haiku 4.5",
    "Threshold logic: 10 or fewer resumes skip scoring, all go to assessment",
    "More than 10 resumes: LLM scores and shortlists top candidates",
    "Recruiter dashboard with ranked candidate results and reasons",
])

label("File Handling and Edge Cases")
th2("Scenario", "How We Handle It")
row2("Normal PDF", "PyMuPDF extracts text directly", shade=True)
row2("Scanned PDF with no text layer", "Tesseract OCR reads the image layer")
row2("Image resume (JPG or PNG)", "Tesseract OCR converts image to text", shade=True)
row2("PDF with passport photo inside", "PyMuPDF skips image blocks, extracts text only")
row2("Corrupt or unreadable file", "Flagged to recruiter dashboard, skipped from processing", shade=True)
row2("Non-resume file uploaded", "Claude detects it is not a resume and rejects with reason")
pdf.ln(3)

label("LLM Choice and Rationale")
th2("Model", "Role and Reason")
row2("Claude Haiku 4.5", "Primary model: resume parsing, scoring, structured extraction. Cheapest and fastest.", shade=True)
row2("Claude Sonnet", "Fallback only: used for complex or ambiguous resumes where Haiku confidence is low.")
pdf.ln(3)

label("Threshold Logic")
bullet([
    "10 or fewer resumes uploaded  =>  skip LLM scoring, send all to assessment directly",
    "More than 10 resumes  =>  LLM scores each resume vs the JD, shortlists top X%",
    "Shortlist percentage (X%) to be confirmed once open questions are answered",
])

section_header("Open Questions  -  Input Needed Before Architecture is Finalised")
th3("#", "Question", "Why It Matters")
row3("1", "Standalone tool or integrated with Provana / PeopleStrong?", "Core architecture decision", shade=True)
row3("2", "Auth: Provana SSO / Azure AD or simple custom login?", "Determines user access design")
row3("3", "What % of applicants receive the assessment link?", "Sets the shortlist threshold", shade=True)
row3("4", "Notification channel: WhatsApp, email, or both?", "Determines third-party integrations")
row3("5", "How do candidates submit resumes: portal, email dump, or job board?", "Determines ingestion pipeline", shade=True)
pdf.ln(3)

section_header("Phase 2  -  Aptitude Assessment  (Problem Statement Only)")
para(
    "Shortlisted candidates currently take manual aptitude tests administered by the team. "
    "There is no standardization and results are tracked on spreadsheets with no auto-scoring. "
    "Need a digital, auto-scored MCQ engine with randomized question banks, timed tests, "
    "and band classification: Strong, Average, or Reject."
)

section_header("Phase 3  -  Voice Assessment  (Problem Statement Only)")
para(
    "V&A assessment is done via manual phone calls by a dedicated resource. No scalability, "
    "subjective scoring, and no recordings or audit trail. Need an AI-driven voice test that "
    "evaluates communication clarity, fluency, and accent neutrality via speech-to-text analysis. "
    "Results should be auto-scored, recorded, and attached to the candidate profile in the dashboard."
)

divider()
pdf.set_font("Helvetica", "I", 8)
pdf.set_text_color(130, 130, 130)
pdf.multi_cell(
    W, 5,
    "Note: This is a v0.1 discovery document. Architecture, sprint plan, and final tech stack "
    "will be confirmed after the open questions above are resolved.",
    new_x="LMARGIN", new_y="NEXT"
)

output_path = r"C:\Users\ashu.kumar1\Candidate-Screening-Assessment-Bot\PRD_Candidate_Screening_Bot.pdf"
pdf.output(output_path)
print("PDF saved: " + output_path)
