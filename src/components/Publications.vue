<template>
    <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
        <div class="space-y-6 lg:space-y-8">
            <div v-for="(pub, index) in publications" :key="index" 
                class="p-4 lg:p-6 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 bg-white dark:bg-dark-bg-secondary">
                <div class="grid grid-cols-1 lg:grid-cols-[1fr_auto] gap-4 mb-4">
                    <h3 class="text-xl lg:text-2xl font-semibold text-primary dark:text-dark-text">
                        {{ pub.title }}
                    </h3>
                    <span class="italic text-secondary dark:text-dark-text-secondary text-lg lg:text-xl whitespace-nowrap">
                        {{ pub.year }}
                    </span>
                </div>
    
                <p class="text-secondary dark:text-dark-text-secondary mb-3">
                    <span class="font-medium text-primary dark:text-dark-text">Collaborators: </span>
                    <span v-html="formatCollaborators(pub.collaborators)"></span>
                </p>
                <p class="text-secondary dark:text-dark-text-secondary mb-3">
                    <span class="font-medium text-primary dark:text-dark-text">Conference: </span>
                    {{ pub.conference }}
                </p>
                <p v-if="pub.status" class="text-secondary dark:text-dark-text-secondary mb-3">
                    <span class="font-medium text-primary dark:text-dark-text">Status: </span>
                    {{ pub.status }}
                </p>
                <p class="text-secondary dark:text-dark-text-secondary">{{ pub.description }}</p>
            </div>
        </div>
    </div>
    </template>
    
    <script>
    export default {
        name: 'Publications',
        setup() {
            const publications = [
                {
                    title: 'An Unconventional Tale on Sentiment Analysis over Anonymous Online Reporting by the People in Bangladesh during An Outburst Period',
                    collaborators: 'Saman Sadia Saman, MD Tousif Tanjim Anan, Mehedi Hasan, Tanzim Hossain Romel, Muhammad Nasif Imtiaz, Ishika Tarin, Afroza Parvin Disa, Tarik Reza Toha, Jannatun Noor, A. B. M. Alim Al Islam',
                    conference: 'Under Review at CSCW 2025',
                    status: 'Submitted to CSCW 2025',
                    description: "This work explores sentiment analysis of anonymous online reports submitted through uReporter, a pioneering anonymous reporting system in Bangladesh, during a period of social unrest following a tragic incident at a leading engineering university. The researchers collected 124 reports and analyzed them using multiple emotion detection approaches, including lexicon-based analysis and six different language models. The study employed various pre-trained transformer models like RoBERTa and DistilBERT variants, alongside a traditional lexicon-based analyzer using the NRC Emotion Lexicon. To handle multilingual submissions, the researchers used GPT-4 to translate Bengali and Romanized Bengali text to English before analysis. Their findings revealed predominant negative emotions like anger, fear, and sadness across all models, though trust emerged as a surprisingly common emotion in the lexicon analysis. The research highlights both the potential and challenges of emotion detection in anonymous reporting systems, particularly in Global South contexts, and demonstrates how such analysis can provide valuable insights into public sentiment during periods of social upheaval. The study's results suggest that integrating emotion detection into anonymous reporting systems could enhance authorities' understanding of public concerns while maintaining user privacy.",
                    year: 2024
                }
            ]
    
            const formatCollaborators = (collaborators) => {
                return collaborators.split(', ').map(name => {
                    if (name.includes('Muhammad Nasif Imtiaz')) {
                        return `<strong class="text-primary dark:text-dark-text">${name}</strong>`;
                    }
                    return name;
                }).join(', ');
            }
    
            return {
                publications,
                formatCollaborators
            }
        }
    }
    </script>