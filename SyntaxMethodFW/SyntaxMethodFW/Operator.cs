namespace SyntaxMethod {
    public record Operator<T>(string name, Func<T[], List<int>, List<int>, bool, bool> func) where T : Terminal {

        public override string ToString() {
            return name;
        }
    }
}
