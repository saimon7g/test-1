<template>
    <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
        <div class="space-y-6 lg:space-y-8">
            <div v-for="(item, index) in research" :key="index" 
                class="p-4 lg:p-6 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 bg-white dark:bg-dark-bg-secondary">
                <div class="grid grid-cols-1 lg:grid-cols-[1fr_auto] gap-4 mb-4">
                    <h3 class="text-xl lg:text-2xl font-semibold text-primary dark:text-dark-text">
                        {{ item.title }}
                    </h3>
                    <span class="italic text-secondary dark:text-dark-text-secondary text-lg lg:text-xl whitespace-nowrap">
                        {{ item.year }}
                    </span>
                </div>
                
                <p class="text-secondary dark:text-dark-text-secondary mb-3">
                    <span class="font-medium text-primary dark:text-dark-text">Collaborators: </span>
                    <span v-html="formatCollaborators(item.collaborators)"></span>
                </p>
                <p class="text-secondary dark:text-dark-text-secondary">{{ item.description }}</p>
            </div>
        </div>
    </div>
    </template>
    
    <script>
    export default {
        name: 'Research',
        setup() {
            const research = [
                {
                    title: 'Enhancing Conversational AI with Domain Adaptation of Retrieval-Augmented Generation (RAG) Models for Fitness and Nutrition',
                    collaborators: 'Md. Shahriyar Muhaymeen, Nur Uddin Ibne Huda, Md. Jarif Ahsan, Md. Mostofa Akbar',
                    description: "This research explores domain adaptation techniques to enhance Retrieval-Augmented Generation (RAG) models for fitness and nutrition consultation. While Large Language Models (LLMs) exhibit strong generative capabilities, they often struggle with factual accuracy in specialized domains and are prone to hallucinations. To address these challenges, we constructed a domain-specific dataset of over 10,000 curated items covering nutritional values and fitness information, and generated 17,354 verified question-answer pairs. We evaluated four distinct RAG architectures, including RAG-Original, RAG-Finetuned-QA, RAG-DPR-Adapted, and Fusion-in-Decoder, to assess their effectiveness in generating accurate responses for health-related queries. Our evaluation demonstrated that fine-tuning RAG models with domain-specific data significantly improved retrieval accuracy and response reliability, with domain-adapted models achieving higher Exact Match (EM) and F1 scores compared to baseline approaches. The findings highlight the potential of domain-adapted RAG models in developing reliable AI-driven assistants for fitness and nutrition guidance through the integration of retrieval mechanisms with generative capabilities.",
                    year: 2025
                }
            ]
    
            const formatCollaborators = (collaborators) => {
                return collaborators.split(', ').map(name => {
                    if (name.includes('Nur Uddin Ibne Huda')) {
                        return `<strong class="text-primary dark:text-dark-text">${name}</strong>`;
                    }
                    return name;
                }).join(', ');
            }
    
            return {
                research,
                formatCollaborators
            }
        }
    }
    </script>