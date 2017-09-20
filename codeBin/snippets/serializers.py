from rest_framework import serializers
from snippets.models import Snippet, LANGUAGES,STYLECHOICES,LEXERS

"""
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,allow_blank=True,max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    style = serializers.ChoiceField(choices=STYLECHOICES,default='friendly')
    language = serializers.ChoiceField(choices=LANGUAGES,default='python')

    def create(self,validated_data):
        #return validated data given validated Field data
        return Snippet.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""

#Using ModelSerilizers to Serilize JSON Code
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id','title','linenos','language','style','code')
    
