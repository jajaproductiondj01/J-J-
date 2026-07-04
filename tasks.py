from crewai import Task

task1 = Task(
    description="Analyse l'idée musicale de l'utilisateur et propose une structure détaillée pour une track EDM.",
    expected_output="Structure claire avec BPM, genre, éléments clés.",
    agent=grok
)

task2 = Task(
    description="Améliore l'idée avec créativité et émotion.",
    expected_output="Version enrichie de l'idée.",
    agent=claude
)

task3 = Task(
    description="Crée un prompt Suno ultra-détaillé prêt à copier.",
    expected_output="Prompt Suno complet.",
    agent=grok
)

task4 = Task(
    description="Conseils mastering et énergie club.",
    expected_output="Conseils post-production.",
    agent=gemini
)
