library(ggplot2)
muon <- read.delim("muon-decay-events.data")

ggplot(data = muon) + geom_histogram()
