/*
 * Copyright (C) 2014 MineCoders
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 3
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 */

using System;
using System.Collections.Generic;
using System.Text;

public delegate void ProcessCommand(Command cmd);

public struct Command 
{
	public string    Label    { get; private set; }
	public string    Action   { get; private set; }
	public Operand[] Operands { get; private set; }
	public string    Id       { get; private set; }

	public static Command FromString(string str)
	{
		string[] fields = str.Split(' ');
		Command cmd = new Command();

		int idx = 0;
		cmd.Label = (fields.Length == 3) ? fields[idx++] : string.Empty;
		cmd.Action = fields[idx++];

		// Clave para reconocer unívocamente el comando
		StringBuilder id = new StringBuilder(cmd.Action);

		// Procesa los operandos
		string[] ops = fields[idx++].Split(',');
		cmd.Operands = new Operand[ops.Length];
		for (int i = 0; i < ops.Length; i++) {
			if (cmd.Action[0] == 'B') // Salto, es una label
				cmd.Operands[i] = new Operand(ops[i], OperandType.Label);
			else
				cmd.Operands[i] = Operand.FromString(ops[i]);
			id.Append(cmd.Operands[i].Type.ToString()[0]);
		}

		cmd.Id = id.ToString();
		return cmd;
	}

	public override string ToString()
	{
		return string.Format("[Command: Label={0}, Action={1}, Operands={2}, Id={3}]",
			Label, Action, Operands, Id);
	}
}

public struct Operand
{
	public string      Value { get; private set; }
	public OperandType Type  { get; private set; }

	public Operand(string value, OperandType type) : this()
	{
		this.Value = value;
		this.Type  = type;
	}

	/// <summary>
	/// Crea un comando a partir de un string. NO DETECTA LAS LABELS.
	/// </summary>
	/// <returns>The string</returns>
	/// <param name="op">Operand</param>
	public static Operand FromString(string op) 
	{
		if (op[0] == '#')
			return new Operand(op.Substring(1), OperandType.Constant);
		else if (op[0] == '(')
			return new Operand(op.Substring(1, op.Length - 2), OperandType.MemoryPointer);
		else
			return new Operand(op, OperandType.Pointer);
	}
}

public enum OperandType 
{
	Pointer,
	MemoryPointer,
	Constant,
	Label
}

class Solution
{
	private static readonly Dictionary<string, ProcessCommand> Commands =
		new Dictionary<string, ProcessCommand>();

	private byte[] memory;
	private Dictionary<string, Command> commands;

	public Solution(int memSize, Dictionary<string, Command> cmds)
	{
		this.memory   = new byte[memSize];
		this.commands = cmds;
	}

	public static void Main (string[] args)
	{
		// Lee el tamaño de la memoria
		int memSize = Convert.ToInt32(Console.ReadLine(), 16);

		// Lee los comandos
		int i = 0;
		Dictionary<string, Command> cmds = new Dictionary<string, Command>();
		string line = Console.ReadLine();
		while (line != null) {
			Command cmd = Command.FromString(line);
			if (cmd.Label != string.Empty)
				cmds.Add(cmd.Label, cmd);
			else
				cmds.Add(i.ToString(), cmd);

			// Lee la siguiente línea
			line = Console.ReadLine();
			i++;
		}

		// Crea el simulador y comienza
		Solution simulador = new Solution(memSize, cmds);
		simulador.Run();
	}

	public void Run() 
	{

	}
}
