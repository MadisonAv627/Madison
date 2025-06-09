<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>French Revolution D&D Campaign</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #2c3e50, #3498db);
            color: #2c3e50;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        
        .game-container {
            max-width: 800px;
            margin: 0 auto;
            background: #f8f9fa;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            padding: 30px;
            border: 3px solid #8b0000;
        }
        
        .title {
            text-align: center;
            color: #8b0000;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .subtitle {
            text-align: center;
            color: #2c3e50;
            font-size: 1.2em;
            margin-bottom: 30px;
            font-style: italic;
        }
        
        .historical-context {
            background: rgba(220, 53, 69, 0.1);
            padding: 20px;
            border-left: 5px solid #dc3545;
            margin-bottom: 25px;
            border-radius: 5px;
        }
        
        .characters-section {
            margin: 25px 0;
        }
        
        .character-card {
            background: white;
            border: 2px solid #bdc3c7;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .character-card:hover {
            border-color: #8b0000;
            box-shadow: 0 5px 15px rgba(139,0,0,0.3);
            transform: translateY(-2px);
        }
        
        .character-name {
            font-weight: bold;
            color: #8b0000;
            font-size: 1.3em;
            margin-bottom: 5px;
        }
        
        .character-description {
            color: #2c3e50;
            line-height: 1.4;
        }
        
        .game-section {
            display: none;
            margin-top: 20px;
        }
        
        .act-header {
            background: #8b0000;
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 1.4em;
            margin-bottom: 20px;
        }
        
        .choice-section {
            background: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .choice-button {
            background: #3498db;
            color: white;
            border: none;
            padding: 12px 25px;
            margin: 8px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            transition: background 0.3s ease;
        }
        
        .choice-button:hover {
            background: #2980b9;
        }
        
        .resource-management {
            background: #d4edda;
            border: 2px solid #28a745;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .newspaper {
            background: #f8f9fa;
            border: 3px solid #343a40;
            padding: 20px;
            margin: 20px 0;
            font-family: 'Times New Roman', serif;
            border-radius: 5px;
        }
        
        .newspaper-header {
            text-align: center;
            font-size: 1.5em;
            font-weight: bold;
            border-bottom: 2px solid #343a40;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        
        .character-note {
            background: #e9ecef;
            border-left: 5px solid #6c757d;
            padding: 15px;
            margin: 15px 0;
            font-style: italic;
        }
        
        .roll-result {
            background: #f8d7da;
            border: 2px solid #dc3545;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            text-align: center;
            font-weight: bold;
        }
        
        .roll-success {
            background: #d1ecf1;
            border-color: #bee5eb;
        }
        
        .continue-button {
            background: #28a745;
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1em;
            display: block;
            margin: 20px auto;
        }
        
        .continue-button:hover {
            background: #218838;
        }
        
        .final-section {
            background: #fff3cd;
            border: 3px solid #ffc107;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin-top: 30px;
        }
        
        .content-separator {
            border-top: 3px solid #8b0000;
            margin: 25px 0;
            opacity: 0.7;
        }
        
        .resource-title {
            color: #8b0000;
            font-size: 1.3em;
            font-weight: bold;
            margin: 20px 0 15px 0;
        }
        
        .dice-animation {
            font-size: 3em;
            text-align: center;
            margin: 20px 0;
            animation: spin 0.5s ease-in-out;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .roll-display {
            text-align: center;
            margin: 20px 0;
        }
        
        .roll-number {
            font-size: 2em;
            font-weight: bold;
            color: #8b0000;
        }
        
        .roll-equation {
            font-size: 0.9em;
            color: #6c757d;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1 class="title">Vive la Révolution!</h1>
        <p class="subtitle">A French Revolution Survival Campaign</p>
        
        <!-- Character Selection Screen -->
        <div id="character-selection">
            <div class="historical-context">
                <h3>Historical Context - 1789</h3>
                <p>France teeters on the brink of revolution. Years of financial crisis, social inequality, and Enlightenment ideas have created a powder keg. The Third Estate, representing 98% of the population, bears the heaviest tax burden while the nobility and clergy enjoy privileges. King Louis XVI has called the Estates-General for the first time since 1614, desperate for new taxes. The people are hungry, angry, and ready for change. In this turbulent time, survival depends not just on your choices, but on your ability to navigate the shifting political landscape.</p>
            </div>
            
            <div class="characters-section">
                <h3>Choose Your Character:</h3>
                
                <div class="character-card" onclick="selectCharacter('felix')">
                    <div class="character-name">Felix - Revolutionary Woman</div>
                    <div class="character-description">A passionate advocate for women's rights and revolutionary ideals. Cares for young Philip while fighting for political change. Must balance family responsibilities with dangerous political activities.</div>
                </div>
                
                <div class="character-card" onclick="selectCharacter('juquc')">
                    <div class="character-name">Juquc - Constitutional Priest</div>
                    <div class="character-description">A priest torn between religious duty and revolutionary ideals. From noble background but supports the Third Estate. Must navigate the dangerous divide between church and state.</div>
                </div>
                
                <div class="character-card" onclick="selectCharacter('elodie')">
                    <div class="character-name">Elodie - Wealthy Sympathizer</div>
                    <div class="character-description">A woman of means who supports the revolution despite her privileged background. Must hide her wealth while contributing to the cause, risking everything for her beliefs.</div>
                </div>
                
                <div class="character-card" onclick="selectCharacter('antoine')">
                    <div class="character-name">Antoine - Sans-Culotte Leader</div>
                    <div class="character-description">A working-class revolutionary leader, passionate about equality and justice. Commands respect among the poor but must navigate increasingly violent revolutionary politics.</div>
                </div>
                
                <div class="character-card" onclick="selectCharacter('philip')">
                    <div class="character-name">Philip - Revolutionary Child</div>
                    <div class="character-description">Felix's young ward, surviving in revolutionary Paris. Too young for major political decisions but observes everything. Protected from death conditions due to age.</div>
                </div>
            </div>
        </div>
        
        <!-- Game Screen -->
        <div id="game-screen" class="game-section">
            <div id="act-content"></div>
            <div id="newspaper-section" class="newspaper hidden"></div>
            <div id="choice-section" class="choice-section hidden"></div>
            <div id="resource-section" class="resource-management hidden"></div>
            <div id="result-section" class="hidden"></div>
            <button id="continue-btn" class="continue-button hidden" onclick="continueGame()">Continue</button>
        </div>
        
        <!-- Final Screen -->
        <div id="final-screen" class="game-section final-section">
            <div id="final-content"></div>
        </div>
    </div>

    <script>
        let selectedCharacter = '';
        let currentAct = 1;
        let gameState = {
            alive: true,
            connections: {},
            resources: {},
            choices: [],
            failedRolls: 0
        };

        const characters = {
            felix: {
                name: "Felix",
                foodSource: "backyard crops",
                rollType: "Survival",
                modifier: 2,
                connections: ["women's network", "revolutionary contacts"],
                description: "Revolutionary Woman fighting for rights while protecting Philip"
            },
            juquc: {
                name: "Juquc", 
                foodSource: "church connections",
                rollType: "Religion",
                modifier: 2,
                connections: ["church hierarchy", "community charity"],
                description: "Constitutional Priest balancing faith and revolution"
            },
            elodie: {
                name: "Elodie",
                foodSource: "wealth and merchants",
                rollType: "Persuasion", 
                modifier: 2,
                connections: ["merchant network", "hidden wealth"],
                description: "Wealthy Revolutionary hiding her privileged background"
            },
            antoine: {
                name: "Antoine",
                foodSource: "black market",
                rollType: "Streetwise",
                modifier: 2,
                connections: ["sans-culottes", "underground networks"],
                description: "Working-class Revolutionary Leader"
            },
            philip: {
                name: "Philip",
                foodSource: "street skills",
                rollType: "Sleight of Hand",
                modifier: 2,
                connections: ["street network", "Felix's protection"],
                description: "Revolutionary Child under Felix's care",
                protected: true
            }
        };

        const acts = {
            1: {
                title: "ACT 1: REVOLUTIONARY AWAKENING (1789-1791)",
                context: "The Estates-General convenes, leading to the Tennis Court Oath, the storming of the Bastille, and the Declaration of Rights. Revolutionary fervor sweeps France.",
                choices: {
                    felix: {
                        title: "The Tennis Court Oath Decision",
                        description: "The National Assembly gathers at the tennis court after being locked out. Do you support the revolutionary oath?",
                        optionA: "Support the Oath (Gain revolutionary contacts, risk Catholic disapproval)",
                        optionB: "Remain neutral (Safer but lose influence opportunities)",
                        rollRequired: "Constitution +2 to convince Philip this won't endanger family"
                    },
                    juquc: {
                        title: "Revolutionary Allegiance",
                        description: "The National Assembly challenges traditional authority. Where do you stand?",
                        optionA: "Support National Assembly (Align with Antoine, risk noble background exposure)",
                        optionB: "Defend traditional monarchy (Maintain church connections, alienate sans-culottes)",
                        rollRequired: "Deception +3 to hide noble background"
                    }
                }
            },
            2: {
                title: "ACT 2: TERROR AND WAR (1792-1794)",
                context: "The September Massacres, execution of Louis XVI, and the Reign of Terror grip France. The Committee of Public Safety rules with an iron fist.",
                choices: {
                    antoine: {
                        title: "The September Massacres",
                        description: "Mob violence spreads across Paris. Prisoners are being killed in the streets.",
                        optionA: "Participate in 'popular justice' (Gain sans-culottes respect, moral corruption)",
                        optionB: "Try to stop the violence (Risk being labeled counter-revolutionary)",
                        rollRequired: "Intimidation +3 to control mob without joining massacre"
                    },
                    elodie: {
                        title: "Hiding Wealth",
                        description: "The Committee of Public Safety is investigating wealthy citizens. Your fortune is at risk.",
                        optionA: "Hide wealth completely (Safer but lose resources)",
                        optionB: "Use wealth to help revolution (Gain influence but risk exposure)",
                        rollRequired: "Deception +4 to hide remaining wealth"
                    }
                }
            },
            3: {
                title: "ACT 3: WOMEN'S MARCH AND THERMIDOR (1794-1795)",
                context: "The Women's March on Versailles brings the royal family to Paris. Later, Robespierre falls during the Thermidorian Reaction.",
                choices: {
                    felix: {
                        title: "Women's March on Versailles",
                        description: "Economic crisis drives women to march on the royal palace demanding bread and rights.",
                        optionA: "Lead march demands (High risk, high reward)",
                        optionB: "Support march but stay in background (Safer but less influence)",
                        rollRequired: "Charisma +4 to unite different women's factions"
                    },
                    antoine: {
                        title: "Thermidorian Reaction",
                        description: "Robespierre has fallen. What happens to your radical networks?",
                        optionA: "Maintain illegal Jacobin networks (Preserve ideals, risk White Terror)",
                        optionB: "Abandon radical connections (Personal safety, ideological betrayal)",
                        rollRequired: "Stealth +4 to maintain secret meetings"
                    }
                }
            },
            4: {
                title: "ACT 4: DIRECTORY AND NAPOLEON (1795-1799)",
                context: "The Directory struggles with economic instability. Babeuf's communist conspiracy emerges, and Napoleon rises to power.",
                choices: {
                    elodie: {
                        title: "Babeuf's Conspiracy of Equals",
                        description: "A communist conspiracy plans to overthrow the Directory. Will you fund revolution?",
                        optionA: "Fund Babeuf's revolution (Lose everything, maintain ideals)",
                        optionB: "Protect wealth under Directory (Betray revolutionary principles)",
                        rollRequired: "Wisdom +4 to predict conspiracy's success"
                    },
                    felix: {
                        title: "Napoleon's Rise",
                        description: "Napoleon promises stability but threatens revolutionary ideals, especially women's rights.",
                        optionA: "Accept Napoleonic restrictions (Family safety, political retreat)",
                        optionB: "Continue revolutionary activism (Risk family, maintain principles)",
                        rollRequired: "History +3 to understand long-term implications"
                    }
                }
            }
        };

        const newspapers = {
            1: {
                headline: "L'Ami du Peuple - Revolutionary Awakening",
                content: "The Third Estate has declared itself the National Assembly! Citizens storm the Bastille seeking arms and gunpowder. The King's authority crumbles as revolutionary fervor spreads across France. Food riots continue as bread prices soar.",
                note: "From Juquc: 'The church is divided. Some priests embrace revolutionary ideals while others cling to tradition. I pray we can serve both God and the people's cause.'"
            },
            2: {
                headline: "L'Ami du Peuple - Terror Grips Paris",
                content: "The King is executed! War with European monarchies spreads. The Committee of Public Safety implements the Maximum price controls. Citizens report neighbors suspected of counter-revolutionary activities. The guillotine works daily.",
                note: "From Antoine: 'The revolution demands sacrifice. We must be vigilant against enemies within. Every day we grow stronger, but the cost grows heavier.'"
            },
            3: {
                headline: "L'Ami du Peuple - The Tyrant Falls",
                content: "Robespierre and his allies face the guillotine! The Thermidorian Reaction begins as moderates seize control. Churches slowly reopen. Former Jacobins flee or hide. The White Terror begins against radical revolutionaries.",
                note: "From Felix: 'We marched for bread and brought the King to Paris. Now women's voices grow quiet again as men consolidate power. Our revolution is incomplete.'"
            },
            4: {
                headline: "Le Moniteur - The Directory Struggles",
                content: "Economic chaos continues under the Directory. General Bonaparte wins victories in Italy. Babeuf's conspiracy for equality is crushed. The assignat currency collapses. Citizens long for stability and strong leadership.",
                note: "From Elodie: 'I've given much for the cause, but what have we truly achieved? The poor still suffer while new elites emerge. Perhaps some dreams cost too much.'"
            }
        };

        function selectCharacter(character) {
            selectedCharacter = character;
            gameState.connections = {...characters[character].connections};
            document.getElementById('character-selection').style.display = 'none';
            document.getElementById('game-screen').style.display = 'block';
            startGame();
        }

        function startGame() {
            showAct(currentAct);
        }

        function showAct(actNumber) {
            const act = acts[actNumber];
            const actContent = document.getElementById('act-content');
            
            actContent.innerHTML = `
                <div class="act-header">${act.title}</div>
                <div class="historical-context">
                    <h4>Historical Context</h4>
                    <p>${act.context}</p>
                </div>
            `;

            // Show newspaper first
            showNewspaper(actNumber);

            // Add separator line
            setTimeout(() => {
                actContent.innerHTML += '<div class="content-separator"></div>';
                
                // Check if character has a major choice in this act
                if (act.choices && act.choices[selectedCharacter]) {
                    showChoice(act.choices[selectedCharacter]);
                } else {
                    showResourceManagement();
                }
            }, 2000);
        }

        function showNewspaper(actNumber) {
            const newspaper = newspapers[actNumber];
            const newspaperSection = document.getElementById('newspaper-section');
            
            newspaperSection.innerHTML = `
                <div class="newspaper-header">${newspaper.headline}</div>
                <p>${newspaper.content}</p>
                <div class="character-note">
                    <strong>Personal Note:</strong> ${newspaper.note}
                </div>
            `;
            
            newspaperSection.classList.remove('hidden');
        }

        function showChoice(choice) {
            const choiceSection = document.getElementById('choice-section');
            
            choiceSection.innerHTML = `
                <h4>${choice.title}</h4>
                <p>${choice.description}</p>
                <button class="choice-button" onclick="makeChoice('A', '${choice.rollRequired}')">${choice.optionA}</button>
                <button class="choice-button" onclick="makeChoice('B', '${choice.rollRequired}')">${choice.optionB}</button>
            `;
            
            choiceSection.classList.remove('hidden');
        }

        function makeChoice(option, rollRequired) {
            gameState.choices.push({act: currentAct, option: option});
            
            // Roll dice
            const roll = Math.floor(Math.random() * 20) + 1;
            const modifier = parseInt(rollRequired.split('+')[1]) || 0;
            const total = roll + modifier;
            const success = total >= 12; // DC 12 for most rolls
            
            const resultSection = document.getElementById('result-section');
            const rollClass = success ? 'roll-success' : 'roll-result';
            
            resultSection.innerHTML = `
                <div class="${rollClass}">
                    <strong>Roll Required:</strong> ${rollRequired}<br>
                    <strong>Rolled:</strong> ${roll} + ${modifier} = ${total}<br>
                    <strong>Result:</strong> ${success ? 'SUCCESS!' : 'FAILURE!'}
                </div>
                <p>${getChoiceResult(option, success)}</p>
            `;
            
            resultSection.classList.remove('hidden');
            
            if (!success) {
                gameState.failedRolls++;
                if (gameState.failedRolls >= 3 && selectedCharacter !== 'philip') {
                    // Risk of serious consequences
                    if (Math.random() < 0.3) {
                        gameState.alive = false;
                        endGame();
                        return;
                    }
                }
            }
            
            document.getElementById('choice-section').classList.add('hidden');
            document.getElementById('continue-btn').classList.remove('hidden');
        }

        function getChoiceResult(option, success) {
            const results = {
                'A': success ? 
                    "Your bold choice pays off! You gain influence and respect among fellow revolutionaries." :
                    "Your risky decision backfires. You face suspicion and lose some connections.",
                'B': success ?
                    "Your cautious approach proves wise. You maintain your position while avoiding danger." :
                    "Your hesitation is seen as weakness. Others question your commitment to the cause."
            };
            return results[option];
        }

        function showResourceManagement() {
            const character = characters[selectedCharacter];
            const actContent = document.getElementById('act-content');
            
            actContent.innerHTML += `
                <div class="resource-title">Resource Management - Food Acquisition</div>
                <div class="resource-management">
                    <p><strong>${character.name}</strong> must secure food using: <em>${character.foodSource}</em></p>
                    <p>Roll ${character.rollType} +${character.modifier} to maintain food supply</p>
                    <button class="choice-button" onclick="rollForFood()" id="roll-btn">Roll</button>
                    <div id="dice-display" class="hidden"></div>
                    <div id="roll-result-display" class="hidden"></div>
                </div>
            `;
        }

        function rollForFood() {
            const character = characters[selectedCharacter];
            const roll = Math.floor(Math.random() * 20) + 1;
            const total = roll + character.modifier;
            const success = total >= 10; // Lower DC for food rolls
            
            // Hide roll button
            document.getElementById('roll-btn').style.display = 'none';
            
            // Show dice animation
            const diceDisplay = document.getElementById('dice-display');
            const diceSymbols = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];
            diceDisplay.classList.remove('hidden');
            diceDisplay.className = 'dice-animation';
            
            // Animate through dice faces
            let animationCount = 0;
            const animationInterval = setInterval(() => {
                diceDisplay.innerHTML = diceSymbols[Math.floor(Math.random() * 6)];
                animationCount++;
                
                if (animationCount >= 10) {
                    clearInterval(animationInterval);
                    
                    // Show final dice face based on roll
                    const finalDice = roll <= 6 ? diceSymbols[roll - 1] : diceSymbols[5];
                    diceDisplay.innerHTML = finalDice;
                    
                    // After brief pause, show result
                    setTimeout(() => {
                        diceDisplay.classList.add('hidden');
                        showRollResult(roll, total, success, character);
                    }, 1000);
                }
            }, 100);
        }
        
        function showRollResult(roll, total, success, character) {
            const rollResultDisplay = document.getElementById('roll-result-display');
            
            let result = '';
            if (success) {
                result = `You successfully acquire food! Your ${character.foodSource} provides enough sustenance.`;
            } else {
                result = `Food is scarce! Your attempt to use ${character.foodSource} fails. You go hungry this month.`;
                gameState.failedRolls++;
                
                if (selectedCharacter !== 'philip' && gameState.failedRolls >= 3) {
                    result += " You are beginning to weaken from hunger...";
                }
            }
            
            rollResultDisplay.innerHTML = `
                <div class="roll-display">
                    <div class="roll-number">You rolled a ${roll}! ${success ? 'SUCCESS!' : 'FAILURE!'}</div>
                    <div class="roll-equation"><strong>Rolled:</strong> ${roll} + ${character.modifier} = ${total}</div>
                </div>
                <p>${result}</p>
            `;
            
            rollResultDisplay.classList.remove('hidden');
            document.getElementById('continue-btn').classList.remove('hidden');
        }

        function continueGame() {
            currentAct++;
            
            if (currentAct <= 4) {
                // Reset for next act
                document.getElementById('newspaper-section').classList.add('hidden');
                document.getElementById('result-section').classList.add('hidden');
                document.getElementById('continue-btn').classList.add('hidden');
                showAct(currentAct);
            } else {
                endGame();
            }
        }

        function endGame() {
            document.getElementById('game-screen').style.display = 'none';
            document.getElementById('final-screen').style.display = 'block';
            
            const character = characters[selectedCharacter];
            let finalContent = '';
            let deathCause = '';
            let finalLine = '';
            
            // Generate autobiography based on choices and death conditions
            let autobiography = `
                <div class="autobiography">
                    <div class="autobiography-header">L'Ami du Peuple - Revolutionary Memoir</div>
                    <p><strong>The Revolutionary Journey of ${character.name}</strong></p>
                    <p><em>A Chronicle of Survival and Sacrifice (1789-1799)</em></p>
                    <br>
            `;
            
            // Add choice descriptions
            gameState.choices.forEach((choice, index) => {
                const actNum = choice.act;
                const option = choice.option;
                const choiceText = option === 'A' ? 'chose the bold path of direct action' : 'took the cautious route of measured response';
                autobiography += `<p><strong>Act ${actNum}:</strong> During the tumultuous events of ${acts[actNum].title.split(':')[1]}, ${character.name} ${choiceText}, demonstrating their commitment to their revolutionary ideals.</p>`;
            });
            
            // Determine death cause and final assessment
            if (!gameState.alive && selectedCharacter !== 'philip') {
                if (gameState.failedRolls >= 3) {
                    deathCause = 'famine';
                    finalLine = 'Game Failure - Revolutionary ideals could not overcome the harsh realities of survival.';
                } else {
                    deathCause = 'political persecution and exile';
                    finalLine = 'Game Failure - The revolution claimed another victim to its violent passions.';
                }
                autobiography += `<p><strong>Final Days:</strong> ${character.name}'s revolutionary journey ended tragically through ${deathCause}. Their sacrifice was not in vain, as their example inspired others to continue the fight for liberty and equality.</p>`;
            } else {
                deathCause = 'old age';
                finalLine = 'Successful Run - A life well-lived in service to revolutionary ideals and the common good.';
                autobiography += `<p><strong>Legacy:</strong> ${character.name} survived the revolutionary period and lived to see the transformation of France. They died peacefully in ${deathCause}, having witnessed the birth of a new world.</p>`;
            }
            
            autobiography += `<p><strong>Final Assessment:</strong> ${finalLine}</p>`;
            autobiography += '</div>';
            
            if (!gameState.alive && selectedCharacter !== 'philip') {
                finalContent = `
                    <h2>Your Revolution Ends</h2>
                    <p><strong>${character.name}</strong> did not survive the tumultuous years of the French Revolution. Their story serves as a reminder of the human cost of political transformation.</p>
                    ${autobiography}
                `;
            } else {
                finalContent = `
                    <h2>Congratulations, Citizen!</h2>
                    <p><strong>${character.name}</strong> has survived the French Revolution! Through careful choices, luck, and determination, you navigated one of history's most turbulent periods.</p>
                    
                    ${autobiography}
                    
                    <h3>The Fate of Your Companions</h3>
                    <p><strong>Felix</strong> continued advocating for women's rights, though many gains were lost under Napoleon's rule. She raised Philip to value equality and justice.</p>
                    <p><strong>Juquc</strong> found a way to serve both his faith and his revolutionary ideals, helping to heal the wounds between church and state in post-revolutionary France.</p>
                    <p><strong>Elodie</strong> used her remaining wealth to establish schools and charities, proving that privilege could serve the common good.</p>
                    <p><strong>Antoine</strong> remained active in underground political movements, keeping revolutionary ideals alive through the Napoleonic era.</p>
                    <p><strong>Philip</strong> grew up to become a chronicler of the revolution, recording the stories of those who lived through these extraordinary times.</p>
                    
                    <h3>France's Future</h3>
                    <p>The revolution transformed France forever. Though Napoleon's rise marked the end of the revolutionary period, the ideals of liberty, equality, and fraternity continued to inspire democratic movements worldwide. Your participation in these events helped shape the modern world.</p>
                    
                    <p><em>The revolution lives on in the hearts of those who dare to dream of a better world.</em></p>
                `;
            }
            
            finalContent += '<button class="restart-button" onclick="restartGame()">Return to Start</button>';
            
            document.getElementById('final-content').innerHTML = finalContent;
        }
        
        function restartGame() {
            // Reset all game state
            selectedCharacter = '';
            currentAct = 1;
            gameState = {
                alive: true,
                connections: {},
                resources: {},
                choices: [],
                failedRolls: 0
            };
            
            // Show character selection screen
            document.getElementById('final-screen').style.display = 'none';
            document.getElementById('character-selection').style.display = 'block';
        }
    </script>
</body>
</html>
