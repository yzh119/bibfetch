// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import { execSync } from 'child_process';
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	console.log('Congratulations, your extension "bibfetch" is now active!');
	const config = vscode.workspace.getConfiguration('');
	let defaultBackend: string = config.get("bibfetch.defaultBackend", "dblp");
	let defaultNumEntries: number = config.get("bibfetch.defaultNumEntries", 10);
	let pyCommand = config.get("bibfetch.pythonpath", "python3");

	// Check if the Python package is installed.
	try {
			execSync(`${pyCommand} -m pip show bibfetch`);
	} catch (error) {
			vscode.window.showErrorMessage('bibfetch python package is not installed.' +
																		 ' Please run "pip3 install bibfetch" and reload the window');
			return ;
	}

	let callBibfetch = (paperTitle: string, backend: string, numEntries: number) => {
		try {
			let outputBuf = execSync(`${pyCommand} -m bibfetch -t "${paperTitle}" -b ${backend} -n ${numEntries}`);
			vscode.window.showInformationMessage("bibfetch successfully fetched the bibtex entries.");
			vscode.workspace.openTextDocument({
				content: outputBuf.toString(),
				language: "bibtex",
			}).then(vscode.window.showTextDocument);
		} catch (error) {
			vscode.window.showErrorMessage("bibfetch failed to fetch the bibtex entries. error message: " + error);
		}
	};

	let disposableSearchBibtexWith = vscode.commands.registerCommand('bibfetch.searchBibtexWith', async () => {
		let paperTitle = await vscode.window.showInputBox({
			placeHolder: "Type the title of the paper",
			prompt: "Search bibtex of an article with custom setting.",
		});
		if (paperTitle === '' || paperTitle === undefined) {
			vscode.window.showErrorMessage('A search query is mandatory to execute this action');
		} else {
			let backend = await vscode.window.showQuickPick(['dblp', 'semanticscholar'], {
				placeHolder: "Select the backend academic search engine to use",
			});
			if (backend === '' || backend === undefined) {
				vscode.window.showErrorMessage('A backend is mandatory to execute this action');
			} else {
				let numEntriesStr = await vscode.window.showInputBox({
					placeHolder: "Type the number of entries to fetch",
					value: defaultNumEntries.toString(),
				});
				if (numEntriesStr === '' || numEntriesStr === undefined) {
					vscode.window.showErrorMessage('A number of entries is mandatory to execute this action');
				} else {
					if (isNaN(+numEntriesStr)) {
						vscode.window.showErrorMessage('The number of entries must be a number');
					} else {
						let numEntries: number = +numEntriesStr;
						callBibfetch(paperTitle, backend, numEntries);
					}
				}
			}
		}
	});

	let disposableSearchBibtexDefault = vscode.commands.registerCommand('bibfetch.searchBibtexDefault', async () => {
		let paperTitle = await vscode.window.showInputBox({
			placeHolder: "Type the title of the paper",
			prompt: "Search bibtex of an article with default setting.",
		});
		if (paperTitle === '' || paperTitle === undefined) {
			vscode.window.showErrorMessage('A search query is mandatory to execute this action');
		} else {
			callBibfetch(paperTitle, defaultBackend, defaultNumEntries);
		}
	});

	let disposableSearchBibtexForSelectedText = vscode.commands.registerCommand('bibfetch.searchBibtexForSelectedText', async () => {
		// source: https://github.com/microsoft/vscode-extension-samples/blob/f1df8faee789ed72a42010a42e10bc9baf624929/document-editing-sample/src/extension.ts#L8-L20
		var editor = vscode.window.activeTextEditor;
		if (!editor) {
			return; // No open text editor
		}
		var paperTitle = editor.document.getText(editor.selection);
		callBibfetch(paperTitle, defaultBackend, defaultNumEntries);
	});

	context.subscriptions.push(disposableSearchBibtexWith, disposableSearchBibtexDefault, disposableSearchBibtexForSelectedText);
}

// This method is called when your extension is deactivated
export function deactivate() { }
