namespace SyntaxMethodFW {
    partial class Main {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.tbTerminalsFile = new System.Windows.Forms.TextBox();
            this.tbRulesFile = new System.Windows.Forms.TextBox();
            this.btnSet = new System.Windows.Forms.Button();
            this.pCanvas = new System.Windows.Forms.Panel();
            this.lStatus = new System.Windows.Forms.Label();
            this.lColor = new System.Windows.Forms.Label();
            this.cbColor = new System.Windows.Forms.ComboBox();
            this.pCanvas.SuspendLayout();
            this.SuspendLayout();
            // 
            // tbTerminalsFile
            // 
            this.tbTerminalsFile.Location = new System.Drawing.Point(497, 12);
            this.tbTerminalsFile.Name = "tbTerminalsFile";
            this.tbTerminalsFile.PlaceholderText = "terms file";
            this.tbTerminalsFile.Size = new System.Drawing.Size(100, 23);
            this.tbTerminalsFile.TabIndex = 1;
            // 
            // tbRulesFile
            // 
            this.tbRulesFile.Location = new System.Drawing.Point(497, 41);
            this.tbRulesFile.Name = "tbRulesFile";
            this.tbRulesFile.PlaceholderText = "rules file";
            this.tbRulesFile.Size = new System.Drawing.Size(100, 23);
            this.tbRulesFile.TabIndex = 2;
            // 
            // btnSet
            // 
            this.btnSet.Location = new System.Drawing.Point(497, 70);
            this.btnSet.Name = "btnSet";
            this.btnSet.Size = new System.Drawing.Size(100, 23);
            this.btnSet.TabIndex = 0;
            this.btnSet.Text = "Load";
            this.btnSet.UseVisualStyleBackColor = true;
            this.btnSet.Click += new System.EventHandler(this.btnSet_Click);
            // 
            // pCanvas
            // 
            this.pCanvas.BackColor = System.Drawing.SystemColors.InactiveCaption;
            this.pCanvas.Controls.Add(this.lStatus);
            this.pCanvas.Controls.Add(this.lColor);
            this.pCanvas.Controls.Add(this.cbColor);
            this.pCanvas.Controls.Add(this.btnSet);
            this.pCanvas.Controls.Add(this.tbTerminalsFile);
            this.pCanvas.Controls.Add(this.tbRulesFile);
            this.pCanvas.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pCanvas.Location = new System.Drawing.Point(0, 0);
            this.pCanvas.Margin = new System.Windows.Forms.Padding(0);
            this.pCanvas.Name = "pCanvas";
            this.pCanvas.Size = new System.Drawing.Size(600, 600);
            this.pCanvas.TabIndex = 4;
            this.pCanvas.Click += new System.EventHandler(this.pCanvas_Click);
            this.pCanvas.Paint += new System.Windows.Forms.PaintEventHandler(this.pCanvas_Paint);
            // 
            // lStatus
            // 
            this.lStatus.AutoSize = true;
            this.lStatus.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.lStatus.Location = new System.Drawing.Point(12, 9);
            this.lStatus.Name = "lStatus";
            this.lStatus.Size = new System.Drawing.Size(0, 28);
            this.lStatus.TabIndex = 5;
            // 
            // lColor
            // 
            this.lColor.AutoSize = true;
            this.lColor.Location = new System.Drawing.Point(349, 547);
            this.lColor.Name = "lColor";
            this.lColor.Size = new System.Drawing.Size(39, 15);
            this.lColor.TabIndex = 4;
            this.lColor.Text = "Color:";
            // 
            // cbColor
            // 
            this.cbColor.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbColor.FormattingEnabled = true;
            this.cbColor.Location = new System.Drawing.Point(349, 565);
            this.cbColor.Name = "cbColor";
            this.cbColor.Size = new System.Drawing.Size(239, 23);
            this.cbColor.TabIndex = 3;
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(600, 600);
            this.Controls.Add(this.pCanvas);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "Main";
            this.Text = "Form1";
            this.pCanvas.ResumeLayout(false);
            this.pCanvas.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private TextBox tbTerminalsFile;
        private TextBox tbRulesFile;
        private Button btnSet;
        private Panel pCanvas;
        private ComboBox cbColor;
        private Label lColor;
        private Label lStatus;
    }
}