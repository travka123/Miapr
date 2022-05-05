namespace SyntaxMethod {
    public class MatrixTerminal : Terminal {

        public int X { get; }
        public int Y { get; }
        public int Value { get; }

        public MatrixTerminal(int x, int y, int value) {
            X = x;
            Y = y;
            Value = value;
        }

        public override int GetValue() {
            return Value;
        }

        public override bool Equals(object? obj) {
            MatrixTerminal? matObj = obj as MatrixTerminal;
            if (matObj == null)
                return false;
            else
                return X == matObj.X && Y == matObj.Y && Value == matObj.Value;
        }

        public override int GetHashCode() {
            return Tuple.Create(X, Y, Value).GetHashCode();
        }

        public static bool Above(MatrixTerminal[] terminals, List<int> a, List<int> b, bool bIsFull) {
            if (a.Select((int i) => terminals[i].Y).Min() - 1 != b.Select((int i) => terminals[i].Y).Max()) {
                return false;
            }

            if (a.Select((int i) => terminals[i].X).Max() < b.Select((int i) => terminals[i].X).Min()) {
                return false;
            }

            if (bIsFull) {
                if (a.Select((int i) => terminals[i].X).Min() > b.Select((int i) => terminals[i].X).Max()) {
                    return false;
                }
            }

            return true;
        }

        public static bool Before(MatrixTerminal[] terminals, List<int> a, List<int> b, bool bIsFull) {
            if (a.Select((int i) => terminals[i].X).Max() != b.Select((int i) => terminals[i].X).Min() - 1) {
                return false;
            }

            if (a.Select((int i) => terminals[i].Y).Min() > b.Select((int i) => terminals[i].Y).Max()) {
                return false;
            }

            if (bIsFull) {
                if (a.Select((int i) => terminals[i].Y).Max() < b.Select((int i) => terminals[i].Y).Min()) {
                    return false;
                }
            }

            return true;
        }
    }
}
