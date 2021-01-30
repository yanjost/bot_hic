#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import discord
import shlex



class Action_Picker():
    _list_embedactions = dict()
    
    @classmethod
    def _assert_actions(cls, actions):
        assert type(actions) is dict, "must enter a dict"
        for k, v in actions.items():
            assert callable(v), "dict must contain functions"
            assert (type(k) is str) and (k.startswith('!')), "dict keys must be strings starting with '!'"
        
    
    def __init__(self, embeds: None):
        if embeds:
            self._assert_actions(embeds)
            self._list_embedactions.update(embeds)
        
    def add_embed(self, embeds):
        self._assert_actions(embeds)
        self._list_embedactions.update(embeds)
        
    
    async def choix_action(self,message):
    
        #si on est dans un salon publique et si on ne commence pas par "!", alors on fait rien
        if str(message.channel.type) == "text":
            if not message.content.startswith("!"):
                return;
    
        
    
            
    
        #début de l'interprétation des commandes
        args = shlex.split(message.content)
    
        action_name = args[0]
        if action_name in self._list_embedactions: #check if it's in the list of Embeds
            action_emb = self._list_embedactions[action_name]
            embed = action_emb()
            
            await message.channel.send(embed=embed)
    
    
    
        else:       
            print("Instruction error")
            embed = discord.Embed()
            embed.title = "Erreur"
            embed.description = "Instruction non valable - Entrez `!aide` pour obtenir l'aide"
            await message.channel.send(embed=embed)





def show_help():
    
    embed = discord.Embed()
    
    msg = ""
    msg += "==== Hacking Industry Camp - AIDE ====\n"
    msg += "- `!aide` : obtenir l'aide\n"
    
    
    field_name = "Aide"
    embed.add_field(name=field_name,value=msg)

    return embed