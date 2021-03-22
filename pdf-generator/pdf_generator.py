import os
import win32com.client as win32


class PDFGenerator:
    def __init__(self):
        self.message = "Program started..."
        self.working_directory = os.getcwd()
        self.data_source = os.path.join(self.working_directory, "data", "data.xlsx")
        self.template = os.path.join(self.working_directory, "template", "Letter Template.docx")
        self.destination_folder = os.path.join(self.working_directory, "output")
        self.word_application = win32.Dispatch("Word.Application")
        self.source_document = None
        self.mail_merge = None,
        self.record_count = 0

    def start(self):
        self.print_start_message()
        self.open_word_template()
        self.perform_mail_merge()
        self.close_word_template()
        self.print_finish_message()

    def print_start_message(self):
        print(f"{self.message}")

    def open_word_template(self):
        print("Opening Word...")
        print("Switch to Word and click OK.")

        self.word_application.Visible = True

        self.source_document = self.word_application.Documents.Open(
            self.template
        )

        self.mail_merge = self.source_document.MailMerge
        self.mail_merge.OpenDataSource(
            Name := self.data_source,
            sqlstatement := "SELECT * FROM [data$]"
        )

        self.record_count = self.mail_merge.DataSource.RecordCount

    def perform_mail_merge(self):
        for i in range(1, self.record_count + 1):
            self.set_active_records(i)

            self.mail_merge.Destination = 0
            self.mail_merge.Execute(False)

            base_name = self.mail_merge.DataSource.DataFields(
                "Name of Recipient".replace(" ", "_")).Value

            print(f"PDF {i} ({base_name}) generated.")

            self.save_and_close_file(base_name)

    def save_and_close_file(self, base_name: str):
        target_document = self.word_application.ActiveDocument
        target_document.SaveAs2(
            os.path.join(
                self.destination_folder, base_name + ".docx"),
            16
        )
        target_document.ExportAsFixedFormat(
            os.path.join(self.destination_folder, base_name),
            exportformat := 17
        )
        target_document.Close(False)
        target_document = None

    def set_active_records(self, i: int):
        self.mail_merge.DataSource.ActiveRecord = i
        self.mail_merge.DataSource.FirstRecord = i
        self.mail_merge.DataSource.LastRecord = i

    def close_word_template(self):
        self.source_document.MailMerge.MainDocumentType = -1

    def print_finish_message(self):
        print("PDFs saved to " + self.destination_folder)
