using SyntaxMethod;

namespace SyntaxMethodFW {
    public partial class Main : Form {

        static readonly int fieldSize = 10;

        G<MatrixTerminal>? grammar;

        List<MatrixTerminal> terminals = new();

        public Main() {
            InitializeComponent();
            pCanvas.CreateGraphics();
        }

        private void btnSet_Click(object sender, EventArgs e) {
            grammar = new(tbTerminalsFile.Text, tbRulesFile.Text, new List<Operator<MatrixTerminal>>() {
            //grammar = new(@"C:\Users\User\source\repos\SyntaxMethod\plane_terms.txt", @"C:\Users\User\source\repos\SyntaxMethod\plane_rules.txt", new List<Operator<MatrixTerminal>>() {
                new("над", MatrixTerminal.Above),
                new("перед", MatrixTerminal.Before),
            });

            cbColor.Items.Clear();
            foreach (var terminal in grammar.GetTerminals()) {
                cbColor.Items.Add(terminal);
            }
            cbColor.SelectedIndex = 0;

            terminals.Clear();

            lStatus.Text = "";

            pCanvas.Invalidate();
        }

        private void pCanvas_Paint(object sender, PaintEventArgs e) {
            foreach (var terminal in terminals) {

                Brush brush = new SolidBrush(Color.FromArgb(terminal.Value));

                var rectangle = RectangleFromCellCords(terminal.X, terminal.Y);

                e.Graphics.FillRectangle(brush, rectangle);        
            }
        }

        private Rectangle RectangleFromCellCords(int cellX, int cellY) => new Rectangle(
                (int)((float)cellX / fieldSize * pCanvas.Width),
                (int)((float)(fieldSize - cellY - 1) / fieldSize * pCanvas.Height),
                pCanvas.Width / fieldSize,
                pCanvas.Height / fieldSize
            );

        private void pCanvas_Click(object sender, EventArgs e) {

            if (grammar != null) {

                var color = (Token)cbColor.SelectedItem;

                var information = (MouseEventArgs)e;
                if (information.Button == MouseButtons.Left || information.Button == MouseButtons.Right) {

                    var (cellX, cellY) = GetCellCords(information.X, information.Y);

                    if (InField(cellX, cellY)) {

                        RemoveTerminal(cellX, cellY);

                        if (information.Button == MouseButtons.Left) {

                            terminals.Add(new MatrixTerminal(cellX, cellY, color.Value));

                        }

                        lStatus.Text = "Processing";

                        if (grammar.Verify(terminals.ToArray())) {
                            lStatus.Text = "Match";
                        }
                        else {
                            lStatus.Text = "Does not match";
                        }

                        pCanvas.Invalidate();
                    } 
                }
            }
        }

        private (int x, int y) GetCellCords(int x, int y) {
            return (x * fieldSize / pCanvas.Width, fieldSize - y * fieldSize / pCanvas.Height - 1);
        }

        private void RemoveTerminal(int cellX, int cellY) {

            var terminal = terminals.Find(t => t.X == cellX && t.Y == cellY);

            if (terminal != null) {

                terminals.Remove(terminal);

            }
        }

        private bool InField(int x, int y) {
            return (x >= 0) && (y >= 0) && (x < fieldSize) && (y < fieldSize);
        }
    }
}