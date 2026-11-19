// Power Query (M): Fact_Production
// Change the file path to where you saved data/powerbi/Fact_Production.csv
let
    Source = Csv.Document(File.Contents("C:\Project\Fact_Production.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {{"Year", Int64.Type}, {"Item_ID", Int64.Type}, {"Area_Harvested", type number}, {"Production", type number}, {"Yield", type number}, {"Production_Level", type text}, {"Period", type text}}),
    NoDupes = Table.Distinct(Typed, {"Year", "Item_ID"})
in
    NoDupes
