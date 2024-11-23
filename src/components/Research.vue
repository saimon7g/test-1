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
                    title: 'Detecting Sentiment in Anonymous Submissions: A Study on User Report Data',
                    collaborators: 'Saman Sadia Saman, MD Tousif Tanjim Anan, Mehedi Hasan, Tanzim Hossain Romel, Muhammad Nasif Imtiaz, Ishika Tarin, Afroza Parvin Disa, Tarik Reza Toha, Jannatun Noor, A. B. M. Alim Al Islam',
                    description: "In this project, we conduct sentiment analysis on crowdsourced, anonymously submitted reports to explore the range and intensity of emotions individuals express when given a platform for open, confidential communication. By performing quantitative analysis across multiple machine learning models, we aim to identify trends in sentiment, uncovering which emotions — such as hatred, anger, relief, or hope — are most commonly conveyed in anonymous complaints. Insights from this study could be valuable for organizations seeking to better understand and respond to community feedback while maintaining the privacy of their contributors.",
                    year: 2024
                },
                {
                    title: 'VLSI Layout Design of Bidirectional Shift Register using Open Source EDA Tools',
                    collaborators: 'Muhammad Nasif Imtiaz, MD. Arafat Hossain, Aman Ray',
                    description: "In this project, we designed and implemented a VLSI layout for a Bidirectional/Circular Shift Register using open-source Electronic Design Automation (EDA) tools. The researchers developed a versatile digital circuit that can function as both a bidirectional shift register and a bidirectional circular shift register, with direction control for left and right shifting operations. The work utilizes Verilog Hardware Description Language (HDL) for implementation and employs the Qflow toolchain along with various open-source tools including Yosys, Graywolf, OpenSTA, QRouter, Netgen, and Magic for the physical layout design. The researchers first implemented and verified the Register Transfer Level (RTL) code through testbenches and waveform analysis using GTKWave. They then generated a gate-level netlist and optimized the VLSI layout using standard cell libraries. The study also includes power consumption analysis, examining how supply voltage and clock frequency affect the circuit's average power consumption. Results show an upward trend in power consumption with increasing supply voltage and a downward trend with increasing clock frequency. The research demonstrates the feasibility and effectiveness of using open-source EDA tools for implementing complex digital circuits, providing a cost-effective alternative to proprietary tools while maintaining design efficiency and optimization.",
                    year: 2023
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
                research,
                formatCollaborators
            }
        }
    }
    </script>