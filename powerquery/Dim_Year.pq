// Power Query (M): Dim_Year (a blank query, 1961 to 2024)
let
    Years = List.Numbers(1961, 64),
    T = Table.FromList(Years, Splitter.SplitByNothing(), {"Year"}),
    Typed = Table.TransformColumnTypes(T, {{"Year", Int64.Type}}),
    Decade = Table.AddColumn(Typed, "Decade", each Number.IntegerDivide([Year], 10) * 10, Int64.Type)
in
    Decade
