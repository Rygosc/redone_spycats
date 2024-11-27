from rest_framework import serializers
from .models import SpyCat, Mission, Target 


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ["id", "name", "years_of_experience", "breed", "salary"]


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "mission", "name", "country", "notes", "complete"]


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ["id", "cat", "complete", "created_at", "updated_at", "targets"]

    def create(self, validated_data):
        targets_data = validated_data.pop("targets", [])
        mission = Mission.objects.create(
            **validated_data
        )
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)

        mission.refresh_from_db()
        return mission
