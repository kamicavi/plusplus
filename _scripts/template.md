---
{{ content.yaml -}}
---
{{ content.description | urlize() }}

{% if content.projects %}
## Example projects
{{ content.projects | urlize() }}
{% endif %} 

{% if content.resources %}
## Resources
{{ content.resources | urlize() }}
{% endif %}