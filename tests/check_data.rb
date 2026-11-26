require "yaml"
require "bibtex"

areas = YAML.safe_load_file("_data/research_areas.yml")
keys = BibTeX.open("_bibliography/papers.bib").entries.keys
seen = {}
ids = areas.map { |area| area.fetch("id") }
abort "Research IDs must be unique" unless ids.uniq == ids
abort "Research IDs and paper IDs must not collide" unless (ids & keys).empty?
anchor = /\A[A-Za-z0-9][A-Za-z0-9._:-]*\z/
(areas.flat_map { |area| [area["id"], *area.fetch("papers")] } + keys).each do |id|
  abort "Invalid anchor: #{id.inspect}" unless anchor.match?(id)
end

areas.each do |area|
  group = area.fetch("id")
  papers = area.fetch("papers")
  papers.each do |paper|
    abort "Unknown BibTeX entry #{paper} in #{group}" unless keys.include?(paper)
    abort "Paper #{paper} appears more than once (#{seen[paper]} and #{group})" if seen.key?(paper)
    seen[paper] = group
  end
  area.fetch("highlights", []).each do |highlight|
    paper = highlight.fetch("key")
    abort "Highlight #{paper} is not in its own research group (#{group})" unless papers.include?(paper)
  end
end
abort "Ungrouped papers: #{(keys - seen.keys).join(', ')}" unless (keys - seen.keys).empty?
puts "Verified #{keys.size} BibTeX entries across #{areas.size} research groups"
